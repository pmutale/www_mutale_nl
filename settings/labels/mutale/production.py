from settings.labels.mutale.base import *
import dj_database_url

from themes import secrets

DEBUG = False

ALLOWED_HOSTS = ['mutale.herokuapp.com', '127.0.0.1', 'localhost', 'www.mutale.nl', 'stick2uganda.mutale.nl']

DATABASE_URL = 'postgres://oogcsuzgfwhqbc:0da4b0d51b2f508e4c00308e3c583c2dd9999b6b439a5501dcd643602b455167@ec2-54' \
               '-247-92-185.eu-west-1.compute.amazonaws.com:5432/dmtkic08buj90'

# DATABASE_URL = 'postgres://zqspeetvbbryuv:6b61e8ca56fcae5efe9a36dd06969fa7aa7aab8205f8104fb1faf76245676655@ec2-79-' \
#                '125-2-71.eu-west-1.compute.amazonaws.com:5432/dfe5phk7q3gn23'
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

