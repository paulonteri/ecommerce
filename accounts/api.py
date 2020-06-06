from django.contrib.auth.models import Group, Permission
from knox.models import AuthToken
from rest_framework import generics, permissions, viewsets
from rest_framework.exceptions import APIException, MethodNotAllowed
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer, \
    GroupSerializer, PermissionSerializer


class RegisterAPI(generics.GenericAPIView):
    """
    Register API
    """
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = RegisterSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        if not "groups" in request.data or len(request.data["groups"]) < 1:
            # raise APIException("User must be in at least one group!")
            pass
        else:
            serializer = self.get_serializer(data=request.data)
        # send back any errors
        serializer.is_valid(raise_exception=True)
        # save user
        user = serializer.save()
        # save groups
        user.groups.set(request.data["groups"])

        # send response
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            # create and send back token
            "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(generics.GenericAPIView):
    """
    Login API
    """
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny, ]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # send back any errors
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        # send response(RF) back
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            # create and send back token
            "token": AuthToken.objects.create(user)[1]
        })


class UserAPI(generics.RetrieveAPIView):
    """
    Get User API
    """
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer

    def get_object(self):
        # get user using the token in isAuthenticated
        return self.request.user


class UpdateUserAPI(viewsets.ModelViewSet):
    """
    Update API
    """

    permission_classes = [permissions.DjangoModelPermissions, permissions.IsAdminUser]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    grps = None

    def perform_create(self, serializer):
        raise MethodNotAllowed(list, "Not Alllowed")

    def perform_destroy(self, instance):
        raise MethodNotAllowed(list, "Not Alllowed")

    def partial_update(self, request, *args, **kwargs):
        if not "groups" in request.data or len(request.data["groups"]) < 1:
            # raise APIException("User must be in at least one group!")
            pass
        else:
            self.grps = (request.data["groups"])

        return super().partial_update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if not "groups" in request.data or len(request.data["groups"]) < 1:
            # raise APIException("User must be in at least one group!")
            pass
        else:
            self.grps = (request.data["groups"])

        return super().update(request, *args, **kwargs)

    def perform_update(self, serializer):
        #
        instance = serializer.save()
        # save groups
        instance.groups.set(self.grps)
        #
        super().perform_update(serializer)


# user Groups
class GroupAPI(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [
        permissions.DjangoModelPermissions
    ]


# user Permissions
class PermissionAPI(generics.ListAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [
        permissions.DjangoModelPermissions
    ]
