#!/usr/bin/env python

import sys
import os

local_apps = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'local_apps')
emails = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'emails')

if not local_apps in sys.path:
    sys.path.append(local_apps)
    
from djeasytests.testsetup import TestSetup
from aaretur import settings_base

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
            },
        },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
            },
        '': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
            },
        },
    }
    
T_EMAIL_SETTINGS = dict(
    EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend',
    EMAIL_FILE_PATH = 'emails'
)

S_EMAIL_SETTINGS = dict(
    EMAIL_USE_TLS = True,
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend',
    DEFAULT_FROM_EMAIL = '',
    SERVER_EMAIL = '',
    EMAIL_PORT = 587,
    EMAIL_HOST = '',
    EMAIL_HOST_USER = '',
    EMAIL_HOST_PASSWORD = ''

)
settings = dict(
    DEBUG=True,
    STATIC_ROOT=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'aaretur', 'static'),
    LOGGING=LOGGING,
    **T_EMAIL_SETTINGS
)

testsetup = TestSetup(appname='aaretur', test_settings=settings, fallback_settings=settings_base)

if __name__ == '__main__':
    testsetup.run(__file__)
