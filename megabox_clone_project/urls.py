from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import refresh_jwt_token, verify_jwt_token, obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies', include('movie.urls')),
    path('users', include('user.urls')),
    path('jwt-auth/', obtain_jwt_token),  # 로그인 & JWT 토큰 획득
    path('jwt-auth/refresh/', refresh_jwt_token),  # JWT 토큰 갱신
    path('jwt-auth/verify/', verify_jwt_token),   # JWT 토큰 확인
    path('reservations', include('reservation.urls')),
]
