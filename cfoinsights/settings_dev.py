import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cfoinsights',
        'USER': 'admin',
        'PASSWORD': 'nissemand95',
        'HOST': 'localhost',
        'PORT': '',
    }
}

ALLOWED_HOSTS = ['*']

DEBUG = True


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

PREPEND_WWW = False