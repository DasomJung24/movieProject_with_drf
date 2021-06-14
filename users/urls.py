from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, UserLoginView, UserSignUpView, confirm_email

router = DefaultRouter(trailing_slash=False)

router.register(r'users', UserViewSet)

urlpatterns = [
    path('signup', UserSignUpView.as_view(), name='signup'),
    path('login', UserLoginView.as_view(), name='login'),
    path('confirm-email', confirm_email, name='confirm-email'),
]
urlpatterns += router.urls
