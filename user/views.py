from rest_framework import viewsets, permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import User
from .serializers import UserSignUpSerializer, UserUpdateSerializer


class UserSignUpViewSet(viewsets.ModelViewSet):
    serializer_class = UserSignUpSerializer
    permission_classes = [permissions.AllowAny]
    model = User


class UserUpdateViewSet(viewsets.ModelViewSet):
    serializer_class = UserUpdateSerializer
    authentication_classes = [JSONWebTokenAuthentication]
    model = User

    def dispatch(self, request, *args, **kwargs):
        print(request.headers)
        return super().dispatch(request, *args, **kwargs)