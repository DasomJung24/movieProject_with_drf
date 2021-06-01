from rest_framework import viewsets, permissions, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from megabox_clone_project.utils import IsOwnerOrReadOnly
from .models import User
from .serializers import UserSignUpSerializer, UserSerializer, UserLoginSerializer


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
    authentication_classes = [IsOwnerOrReadOnly]
    model = User
    queryset = User.objects.all()

    def get_object(self):
        return self.queryset.get(pk=self.request.user.id)

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.user)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
