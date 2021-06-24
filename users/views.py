from rest_framework import viewsets, permissions, status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from megabox_clone_project.utils import IsOwnerOrReadOnly
from .models import User, FavoriteTheater
from .serializers import UserSignUpSerializer, UserSerializer, UserLoginSerializer


class UserSignUpView(generics.CreateAPIView):
    serializer_class = UserSignUpSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        context = {
            'data': request.data
        }
        serializer = self.serializer_class(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserLoginView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.prefetch_related('favorites', 'favorites__theater', 'likes', 'likes__movie')

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserView(APIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()

    def get_object(self):
        return self.queryset.get(pk=self.request.user.id)

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user, many=False)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def confirm_email(request):
    if User.objects.filter(email=request.data['email']):
        return Response({'email': True, 'data': request.data})
    else:
        return Response({'email': False, 'data': request.data})
