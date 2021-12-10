from .base import *

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',

    }
}