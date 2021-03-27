from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReservationMainViewSet.as_view({'get': 'list'}), name='reservation_main'),
    path('/<int:theater_id>', views.TheaterTodayViewSet.as_view({'get': 'list'}), name='today_movies'),
]