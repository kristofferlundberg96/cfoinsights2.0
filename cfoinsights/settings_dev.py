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