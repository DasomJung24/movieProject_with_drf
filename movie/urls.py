from django.urls import path
from . import views

urlpatterns = [
    path('', views.MovieViewSet.as_view({'get': 'list'}), name='movie_list'),
]