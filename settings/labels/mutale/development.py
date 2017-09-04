from settings.labels.mutale.base import *


DEBUG = True

ALLOWED_HOSTS = ['mutale.herokuapp.com', '127.0.0.1', 'localhost']

SECRET_KEY = 'qs7s_mqq@1d6uz%rj@q((#p@a^%hzemhhjoh4nolyr^n5t3-k!'

print (SECRET_KEY, 'Peter Mutale')

EMAIL_HOST = 'localhost'

EMAIL_PORT = 1025

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'

EMAIL_FILE_PATH = '/email'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'www_mutale_com',
        'USER': 'pm',
        'PASSWORD': 'COR',
        'HOST': 'localhost',
        'PORT': '',
    }
}

