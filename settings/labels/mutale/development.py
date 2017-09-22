from settings.labels.mutale.base import *

DEBUG = True

ALLOWED_HOSTS = ['mutale.herokuapp.com', '127.0.0.1', 'localhost']

SECRET_KEY = 'qs7s_mqq@1d6uz%rj@q((#p@a^%hzemhhjoh4nolyr^n5t3-k!'

EMAIL_HOST = 'localhost'

EMAIL_PORT = 1025

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'

EMAIL_FILE_PATH = '/email'

DATABASES = {'default': read_pgpass('www_mutale_com'), }

LOGGING['loggers']['django.request'] = {
        'handlers': ['console', 'mail_admins'],
        'level': 'DEBUG',
        'propagate': True,
        }
LOGGING['loggers']['django.db.backends'] = {
        'handlers': ['console'],
        'level': 'INFO',
        'propagate': True,
        }
LOGGING['loggers'][''] = {
        'handlers': ['console'],
        'level': 'INFO',
        'propagate': True,
        }

