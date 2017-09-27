from settings.labels.mutale.base import *

DEBUG = True

ALLOWED_HOSTS = ['mutale.herokuapp.com', '127.0.0.1', 'localhost']

SECRET_KEY = 'qs7s_mqq@1d6uz%rj@q((#p@a^%hzemhhjoh4nolyr^n5t3-k!'

EMAIL_HOST = 'localhost'

EMAIL_PORT = 1025

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'

EMAIL_FILE_PATH = '/email'

DATABASES = {'default': read_pgpass('www_mutale_com'), }

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}

INTERNAL_IPS = ('127.0.0.1',)


def show_toolbar(request):
    return True


DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": show_toolbar,
    "INTERCEPT_REDIRECTS": False,
}
