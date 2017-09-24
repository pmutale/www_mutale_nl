from settings.labels.mutale.base import *
from themes.secrets import read_mailpass

DEBUG = False

ALLOWED_HOSTS = ['mutale.herokuapp.com', '127.0.0.1', 'localhost', 'mutale-dev-a.herokuapp.com',
                 'mutale-prd.herokuapp.com', 'stick2uganda.mutale.nl']

DATABASES = {
    'default':
        read_pgpass('dmtkic08buj90')
}
email_settings = read_mailpass('webmaster@mutale.nl')

DATABASES['default']['CONN_MAX_AGE'] = 500

EMAIL_HOST = email_settings['host']

EMAIL_PORT = email_settings['port']

EMAIL_HOST_USER = email_settings['user']

EMAIL_HOST_PASSWORD = email_settings['password']

EMAIL_USE_SSL = email_settings['ssl']

