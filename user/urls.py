from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.UserSignUpViewSet.as_view({'post': 'create'}), name='signup'),
    path('<int:user_id>', views.UserUpdateViewSet.as_view({'put': 'update'}), name='user_update'),
]