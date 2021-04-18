from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.UserSignUpViewSet.as_view({'post': 'create'}), name='signup'),
    path('profile', views.user_profile, name='user_profile'),
    path('like', views.LikeViewSet.as_view({'post': 'create'}), name='like_create'),
]