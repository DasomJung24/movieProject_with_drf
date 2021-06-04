from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, UserLoginView, UserSignUpView

router = DefaultRouter(trailing_slash=False)

router.register(r'users', UserViewSet)

urlpatterns = [
    path('signup', UserSignUpView.as_view(), name='signup'),
    path('login', UserLoginView.as_view(), name='login'),
]
urlpatterns += router.urls
