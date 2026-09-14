from django.urls import path 
from .views import RegisterUser, ProfileUserView, ChangePasswordView, LogoutView, RegisterUserStaffView, UserAdminView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshSlidingView 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("admin", UserAdminView, name = "admin")


urlpatterns = [
path("register/", RegisterUser.as_view(), name = "register"), 
path("login/", TokenObtainPairView.as_view(), name = "login"),
path("token/refresh/", TokenRefreshSlidingView.as_view(), name = "token-refresh"),
path("Profile/", ProfileUserView.as_view(), name = "profile"),
path("change-password/", ChangePasswordView.as_view(), name = "change-password"),
path("logout/", LogoutView.as_view(), name = "logout"),
path("register-staff/", RegisterUserStaffView.as_view(), name = "register-staff"),
]

urlpatterns += router.urls