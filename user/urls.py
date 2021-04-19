from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.UserSignUpView.as_view(), name='signup'),
    path('login', views.UserLoginView.as_view(), name='login'),
    path('profile', views.user_profile, name='user_profile'),
    path('like', views.LikeViewSet.as_view({'post': 'create'}), name='like_create'),
]