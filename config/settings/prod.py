from .common import *

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJ_APPS

DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]


STATIC_ROOT = os.path.join(PROJ_DIR, "static")