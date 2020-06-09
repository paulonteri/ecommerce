from django.contrib.auth import authenticate
from django.contrib.auth.models import Group, Permission
from rest_framework import serializers

from accounts.models import User


class GroupMinimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["id", "name"]


class UserSerializer(serializers.ModelSerializer):
    """
    User Serializer
    """
    groups = GroupMinimalSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'groups', "date_joined", "last_login")
        depth = 1


class RegisterSerializer(serializers.ModelSerializer):
    """
    Register Serializer
    """

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'], validated_data['email'], validated_data['password'])

        return user


class LoginSerializer(serializers.Serializer):
    """
    Login Serializer
    """
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")


class GroupSerializer(serializers.ModelSerializer):
    """
    Django groups
    https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.Group
    """

    class Meta:
        model = Group
        fields = ["id", "name"]


class GroupSerializerDetailed(serializers.ModelSerializer):
    """
    Django groups
    https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.Group
    """

    class Meta:
        model = Group
        fields = "__all__"
        depth = 2


class PermissionSerializer(serializers.ModelSerializer):
    """
    Django Permissions
    https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.Permission
    """

    def create(self, validated_data):
        raise serializers.ValidationError("Permissions cannot be edited")

    def update(self, instance, validated_data):
        raise serializers.ValidationError("Permissions cannot be edited")

    class Meta:
        model = Permission
        fields = "__all__"
        depth = 1
