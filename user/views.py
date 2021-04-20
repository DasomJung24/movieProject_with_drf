import json

from django.http import JsonResponse
from rest_framework import viewsets, permissions, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import User, Like
from .serializers import UserSignUpSerializer, UserSerializer, LikeSerializer, UserLoginSerializer


class UserSignUpView(generics.CreateAPIView):
    serializer_class = UserSignUpSerializer
    permission_classes = [permissions.AllowAny]
    model = User

    def post(self, request, *args, **kwargs):
        data = request.data.get('user', None)
        data['birth'] = data['birth'].split('T')[0]
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserLoginView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = [permissions.AllowAny]
    model = User

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


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
