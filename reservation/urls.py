from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReservationMainViewSet.as_view({'get': 'list'}), name='reservation_main'),
]