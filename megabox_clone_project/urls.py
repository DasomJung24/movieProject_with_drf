from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework.permissions import AllowAny
from rest_framework_jwt.views import refresh_jwt_token, verify_jwt_token, obtain_jwt_token
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='Megabox Clone API',
        default_version='v1',
        description='Megabox clone project 문서입니다.',
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="jeongdasom6@gmail.com"),
        license=openapi.License(name="Jay's CodeFactory"),
    ),
    validators=['flex'], #'ssv'],
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('movies.urls')),
    path('', include('users.urls')),
    path('reservations', include('reservations.urls')),
    url(r'^swagger(?P<format>\.json|\.yaml)/v1$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/v1/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/v1/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
