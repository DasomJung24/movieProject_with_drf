from django.urls import path

from .views import UserView, UserLoginView, UserSignUpView, confirm_email

urlpatterns = [
    path('signup', UserSignUpView.as_view(), name='signup'),
    path('login', UserLoginView.as_view(), name='login'),
    path('confirm-email', confirm_email, name='confirm_email'),
    path('me', UserView.as_view(), name='me'),
]
