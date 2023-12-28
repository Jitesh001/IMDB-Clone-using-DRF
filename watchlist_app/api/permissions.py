from rest_framework import permissions

    
#only admin has permissions to edit review, other has read only
class AdminOrReadOnly(permissions.IsAdminUser):
    
     def has_permission(self, request, view):
        # Check if the user is an admin
        is_admin = super().has_permission(request, view)

        # Check if the user is a staff user
        is_staff = request.user and request.user.is_staff

        # Allow GET requests and editing (PUT, PATCH, etc.) for admin or staff users
        return request.method == 'GET' or (is_admin or is_staff)
    
#only review user has permissions to edit review, other has read only
class ReviewUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.review_user == request.user or request.user.is_staff