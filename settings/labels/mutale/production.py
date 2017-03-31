from settings.labels.mutale.base import *
import dj_database_url

DEBUG = True

ALLOWED_HOSTS = ['mutale.herokuapp.com', '127.0.0.1']

DATABASE_URL = 'postgres://oogcsuzgfwhqbc:0da4b0d51b2f508e4c00308e3c583c2dd9999b6b439a5501dcd643602b455167@ec2-54' \
               '-247-92-185.eu-west-1.compute.amazonaws.com:5432/dmtkic08buj90'
DATABASES = {
    'default':
        dj_database_url.config(default=DATABASE_URL)
}

DATABASES['default']['CONN_MAX_AGE'] = 500
