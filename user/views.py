import json

from django.http import JsonResponse
from rest_framework import viewsets, permissions
from rest_framework.response import Response
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
    lookup_url_kwarg = 'user_id'
    queryset = User.objects.all()

    def update(self, request, *args, **kwargs):
        data = json.loads(request.body)
        serializer = UserUpdateSerializer(instance=self.get_object(), data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return JsonResponse({'message': 'success'}, status=204)
