from .base import *
import dj_database_url
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['generadorcertamen.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd567mtddg647va',
        'USER': 'glrbposahzvxxq',
        'PASSWORD': '8ae46b76e25c0a13d9c9fc9934a94b1673eb87de50e14e9ce028fb8ef9801ddc',
        'HOST': 'ec2-3-211-228-251.compute-1.amazonaws.com',
        'PORT': 5432,

    }
}

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)