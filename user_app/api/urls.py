from rest_framework.authtoken.views import obtain_auth_token
# from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from django.urls import path, include
from user_app.api import views as account_view

urlpatterns = [
    path('register/', account_view.registration_view, name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('logout/', account_view.logout_view, name='logout'),
]