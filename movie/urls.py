from django.urls import path
from . import views

urlpatterns = [
    path('', views.MovieListView.as_view(), name='movie_list'),
    path('<int:movie_id>', views.MovieDetailView.as_view(), name='movie_detail'),
    path('<int:movie_id>/likes', views.LikeView.as_view(), name='like_create'),
]