from django.urls import path
from .views import TheaterListView

urlpatterns = [
    path('theaters', TheaterListView.as_view()),
]