from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.UserViewSet.as_view({'post': 'create'}), name='signup'),
]