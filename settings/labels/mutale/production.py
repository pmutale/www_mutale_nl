from settings.labels.mutale.base import *
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = ['mutale.herokuapp.com']


db_from_env = dj_database_url.config(conn_max_age=500)

DATABASES['default'].update(db_from_env)
