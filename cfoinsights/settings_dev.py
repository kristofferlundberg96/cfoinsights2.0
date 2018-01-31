import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'cfoinsights', 'static'),
    os.path.join(BASE_DIR, "project/static"),
)

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