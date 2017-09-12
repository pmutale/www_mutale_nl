from settings.labels.mutale.base import *

from themes import secrets

ALLOWED_HOSTS = ['mutale-acc.herokuapp.com', '127.0.0.1', 'localhost']

DATABASE_URL = 'postgres://tchjvyogxumkol:101b8068787cea9f1eb05f0f20abeefe3cf4b5797ccd12f96d5abb8ab3d9d1cb@ec2-79-125' \
               '-26-23.eu-west-1.compute.amazonaws.com:5432/d3dpa9mm8f5aut'
DEBUG = True

DATABASES = {
    'default':
        dj_database_url.config(default=DATABASE_URL)
}

DATABASES['default']['CONN_MAX_AGE'] = 500

EMAIL_HOST = secrets.email_settings['host']

EMAIL_PORT = secrets.email_settings['port']

EMAIL_HOST_USER = secrets.email_settings['user']

EMAIL_HOST_PASSWORD = secrets.email_settings['password']

EMAIL_USE_SSL = secrets.email_settings['ssl']

