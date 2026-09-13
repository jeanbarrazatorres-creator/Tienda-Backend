from rest_framework import serializers 
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenBlacklistSerializer  
from .models import User 

password = serializers.CharField(write_only = True)
password2 = serializers.CharField(write_only = True)

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    password2 = serializers.CharField(write_only = True)
    class Meta:
        model = User 
        fields = ["username", "first_name", "last_name", "email", "password", "password2"]

    def validate(self, data):
        password = data.get("password")
        password2 = data.get("password2")
        if password != password2: 
            raise serializers.ValidationError("password incorrecto")
        return data
        
    def validate_username(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError("Debe tener mas de dos carracteres")
        return value 

    def validate_first_name(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError("Debe tener mas de dos carracteres")
        return value
    
    def validate_last_name(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError("Debe tener mas de dos carracteres")
        return value

    def validate_email(self, value):
        if User.objects.filter(email = value).exists():
            raise serializers.ValidationError("ese email ya esta ocupado")
        return value 

    def validate_password(self, value):
        validate_password(value)
        return value 

    def create(self, validated_data):
        validated_data.pop("password2")
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user 

class ProfileUserSerializer(serializers.ModelSerializer):
    model = User
    fields = ["username", "first_name", "last_name", "email"]


class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(write_only = True )
    new_password = serializers.CharField(write_only = True )
    new_password2 = serializers.CharField(write_only = True )

    def validate_old_password(self, value):
        user = self.context["request"].user
        if not user.check_password(value):
            raise serializers.ValidationError("El password es incorrecto")
        return value
    def validate(self, data):
        new_password = data.get("new_password")
        new_password2 = data.get("new_password2")

        if new_password != new_password2:
            raise serializers.ValidationError("Los password no coinciden")

        validate_password(new_password, self.context["request"].user )
        return data


    class LogoutSerializer(TokenBlacklistSerializer):
        pass