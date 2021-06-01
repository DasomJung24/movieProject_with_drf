from django.urls import path
from . import views

urlpatterns = [
    path('', views.MovieViewSet.as_view({'get': 'list'}), name='movie_list'),
    path('<int:movie_id>', views.MovieDetailViewSet.as_view({'get': 'retrieve'}), name='movie_detail'),
    path('movies/<int:movie_id>/likes', views.LikeViewSet.as_view(), name='like_create'),
]