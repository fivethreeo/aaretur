
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'aaretur',
        'USER': 'aaretur',
        'PASSWORD': 'rds81ro',
        'HOST': '',
        'PORT': ''
    }
}
    
ADMINS = (
    ('Oyvind', 'oyvind.saltvik@gmail.com'),
)

MANAGERS = ADMINS

# Absolute path to the directory that holds media.
STATIC_URL='/static/'
STATIC_ROOT='/home/aaretur/public_html/'
MEDIA_ROOT = '/home/aaretur/public_html/media/'
MEDIA_URL = '/static/media/'

DEBUG = False
TEMPLATE_DEBUG = DEBUG

