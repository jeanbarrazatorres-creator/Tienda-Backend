from django.urls import path 
from .views import RegisterUser 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshSlidingView 

urlpatterns = [
path("register/", RegisterUser.as_view(), name = "register"), 
path("login/", TokenObtainPairView.as_view(), name = "login"),
path("token/refresh/", TokenRefreshSlidingView.as_view(), name = "token-refresh")
]