from .common import *

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJ_APPS

DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]


STATIC_ROOT = os.path.join(PROJ_DIR, "static")


REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.

    "DEFAULT_AUTHENTICATION_CLASSES": [
        'utils.jwt.CustomJwtTokenAuthentication',
        'utils.jwt.SystemKeyAuth',
    ],
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}
