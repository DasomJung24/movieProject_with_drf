from rest_framework import viewsets, permissions

from .models import User
from .serializers import UserSignUpSerializer


class UserSignUpViewSet(viewsets.ModelViewSet):
    serializer_class = UserSignUpSerializer
    permission_classes = (permissions.AllowAny, )
    model = User
