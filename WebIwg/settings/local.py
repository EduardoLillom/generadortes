from .base import *

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db',
        'USER': 'db',
        'PASSWORD': '65f5czWoKSXDJ6X6',
        'HOST': 'app-fdd22719-7cdd-4fd1-ba9e-21890d584c77-do-user-10205479-0.b.db.ondigitalocean.com',
        'DATABASE_PORT': '25060',
    }
}