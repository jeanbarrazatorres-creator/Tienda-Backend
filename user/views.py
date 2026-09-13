from django.shortcuts import render
from rest_framework.generics import CreateAPIView , RetrieveAPIView, CreateAPIView 
from .serializers import UserSerializer, ProfileUserSerializer, ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated

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
        new_password = serializer.validated_data("new_password")
        user.set_password(new_password)
        user.save()





