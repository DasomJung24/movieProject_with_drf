from django.urls import path
from .views import TheaterListView, ScreeningListView

urlpatterns = [
    path('theaters', TheaterListView.as_view()),
    path('theaters/screenings', ScreeningListView.as_view()),
]