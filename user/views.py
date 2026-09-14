from django.shortcuts import render
from rest_framework_simplejwt.views import TokenBlacklistView
from rest_framework.generics import CreateAPIView , RetrieveAPIView, CreateAPIView 
from .serializers import UserSerializer, ProfileUserSerializer, ChangePasswordSerializer, UserStaffSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from .models import User 

class RegisterUser(CreateAPIView):
    serializer_class = UserSerializer 

class ProfileUserView(RetrieveAPIView):
    serializer_class = ProfileUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user 

class ChangePasswordView(CreateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        new_password = serializer.validated_data["new_password"]
        user.set_password(new_password)
        user.save()



class LogoutView(TokenBlacklistView):
    permission_classes = [IsAuthenticated]

class RegisterUserStaffView(CreateAPIView):
    serializer_class = UserStaffSerializer
    permission_classes = [IsAdminUser]


class UserAdminView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserStaffSerializer
    permission_classes = [IsAdminUser]