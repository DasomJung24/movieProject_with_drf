import json

from django.http import JsonResponse
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import User, Like
from .serializers import UserSignUpSerializer, UserSerializer, LikeSerializer


class UserSignUpViewSet(viewsets.ModelViewSet):
    serializer_class = UserSignUpSerializer
    permission_classes = [permissions.AllowAny]
    model = User


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    authentication_classes = [JSONWebTokenAuthentication]
    model = User
    queryset = User.objects.all()

    def get_object(self):
        return self.queryset.get(pk=self.request.user.id)


user_profile = UserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy',
})


class LikeViewSet(viewsets.ModelViewSet):
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]
    model = Like

    def create(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            data['user_id'] = request.user.id
            serializer = LikeSerializer(data)
            if serializer.is_valid():
                like, flag = Like.objects.get_or_create(**data)
                if not flag:
                    like.delete()
                return Response(data)
        except ValueError as e:
            return JsonResponse({'error': '{}'.format(e)}, status=400)
