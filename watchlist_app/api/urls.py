from django.urls import path, include
from rest_framework.routers import DefaultRouter
from watchlist_app.api import views

router = DefaultRouter()
router.register('stream', views.StreamPlatformVS, basename='streamplatform')
#this single route handles everything mentioned in viewset in views.py file
# stream/ - all streams list, stream/id/ - specific stream details

urlpatterns = [
        path('', views.WatchListAV.as_view(), name='watch-list'), 
        path('<int:watch_id>/', views.WatchListDetailAV.as_view(), name='watch-detail'),
        
        path('', include(router.urls)),

        path('<int:watch_id>/review-create/', views.ReviewCreate.as_view(), name='review-create'),
        path('<int:watch_id>/reviews/', views.ReviewList.as_view(), name='review-list'),  
        path('reviews/<int:pk>/', views.ReviewDetail.as_view(), name='review-detail'),
        
        path('user-reviews/', views.UserReview.as_view(), name='user-review-detail'),
        ]
