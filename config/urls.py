#from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from api.accounts import views as account_views

schema_view = get_schema_view(
    openapi.Info(
        title="mdoelviewset 연습",
        default_version='프로젝트 버전 ( 1.0 )',
        description="API 명세서",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

routers = DefaultRouter()

routers.register(r"", account_views.UserViewSet, basename="accounts")

urlpatterns = [
    path(r"api-v1/accounts/", include(routers.urls)),
    path(r"api-v1/accounts/login", account_views.LoginView.as_view()),
    path('__debug__/', include('debug_toolbar.urls')),

    path(r'api-v1/practice/swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(r'api-v1/practice/swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'api-v1/practice/redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



