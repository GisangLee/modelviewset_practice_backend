#from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from api.accounts import views as account_views


routers = DefaultRouter()

routers.register(r"accounts", account_views.UserViewSet)

urlpatterns = [
    path(r"api-v1/", include(routers.urls)),
]

if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]