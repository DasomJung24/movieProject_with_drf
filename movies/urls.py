from django.urls import path
from . import views

urlpatterns = [
    path('movies', views.MovieListView.as_view(), name='movie_list'),
    path('movies/<int:movie_id>', views.MovieDetailView.as_view(), name='movie_detail'),
    path('movies/<int:movie_id>/likes', views.LikeView.as_view(), name='like_create'),
]