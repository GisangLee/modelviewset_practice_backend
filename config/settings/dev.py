from .common import *
import logging as log


THIRD_PARTY_APPS += ["debug_toolbar"]

MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"] + MIDDLEWARE

print(f"THIRD_PARTY_APPS : {THIRD_PARTY_APPS}")
print(f"MIDDLEWARE : {MIDDLEWARE}")


INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJ_APPS

print(f"INSTALLED_APPS : {INSTALLED_APPS}")

DEBUG = True

ALLOWED_HOSTS = []

STATICFILES_DIRS = [os.path.join(PROJ_DIR, "static")]

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.

    # "DEFAULT_AUTHENTICATION_CLASSES": [
    #     'utils.jwt.CustomJwtTokenAuthentication',
    #     'utils.jwt.SystemKeyAuth',
    # ],
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}
