from .common import *

THIRD_PARTY_APPS += ["debug_toolbar"]

MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"] + MIDDLEWARE

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJ_APPS

print(f"써드파티 : {THIRD_PARTY_APPS}")

print(f"미들웨어 : {MIDDLEWARE}")

DEBUG = True

ALLOWED_HOSTS = []

STATICFILES_DIRS = [os.path.join(PROJ_DIR, "static")]