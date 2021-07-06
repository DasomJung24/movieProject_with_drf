from django.urls import path
from .views import TheaterListView, ScreeningListView, get_movies_for_day

urlpatterns = [
    path('theaters', TheaterListView.as_view()),
    path('theaters/screenings', ScreeningListView.as_view()),
    # path('theaters/movies', ScreeningMovieListView.as_view()),
    path('theaters/movies', get_movies_for_day),
]