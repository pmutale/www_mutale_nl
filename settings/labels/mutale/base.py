# -*- coding: utf-8 -*-
from settings.core import *
import dj_database_url
from django.utils.translation import ugettext_lazy as _
from themes import secrets
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'themes', 'static'),
)

SITE_ID = 1

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'mysite', 'templates'), ],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.csrf',
                'django.contrib.messages.context_processors.messages',
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings',
                
                # Own Processors
                'mysite.context_processors.google_analytics',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader'
            ],
        },
    },
]

MIDDLEWARE_CLASSES = (
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware'
)

INSTALLED_APPS = (

    # Django
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',

    # CMS
    'menus',
    'sekizai',
    'treebeard',
    'registration',
    'cms',
    'ckeditor',
    'djangocms_text_ckeditor',
    'filer',
    'easy_thumbnails',
    'djangocms_column',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_utils',
    'djangocms_snippet',
    'djangocms_googlemap',
    'mptt',
    'hvad',
    'debug_toolbar',

    #  Apps
    'mysite',
    'themes',
    'stick2uganda',
    'rosetta',
)

LANGUAGES = (
    ('en', _('English')),
    ('nl', _('Nederlands')),
    ('sw', _('Swahili')),
)

CMS_LANGUAGES = {
    'default': {
        'public': True,
        'hide_untranslated': False,
        'redirect_on_fallback': True,
    }
}

CMS_TEMPLATES = (
    ('themes/partials/homepage.html', 'HomePage'),
    ('sidebar_left.html', 'Sidebar Left'),
    ('sidebar_right.html', 'Sidebar Right')
)

CMS_PERMISSION = True

CKEDITOR_UPLOAD_PATH = 'content/ckeditor/uploads'

CMS_PLACEHOLDER_CONF = {}

MIGRATION_MODULES = {

}

def read_pgpass(dbname):
    import os
    try:
        pgpass = os.path.join(os.environ['HOME'], '.pgpass')
        pgpass_lines = open(pgpass).read().split()
    except IOError:
        pass
    else:
        for match in (dbname, '*'):
            for line in pgpass_lines:
                words = line.strip().split(':')
                if words[2] == match:
                    return {
                        'ENGINE': 'django.db.backends.postgresql_psycopg2',
                        'NAME': dbname,
                        'USER': words[3],
                        'PASSWORD': words[4],
                        'HOST': words[0],
                    }
    return {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'var', '%s.db' % dbname),
    }

# CMS_TOOLBAR_ANONYMOUS_ON = False

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)
THUMBNAIL_HIGH_RESOLUTION = True

DATE_INPUT_FORMATS = '%Y/%m/%d'

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

STATICFILESTORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

WSGI_APPLICATION = 'mysite.wsgi.application'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

DEFAULT_FROM_EMAIL = 'webmaster@mutale.nl'

CMSPLUGIN_FILER_IMAGE_STYLE_CHOICES = (
    ('default', 'Default'),
    ('boxed', 'Boxed'),
)
CMSPLUGIN_FILER_IMAGE_DEFAULT_STYLE = 'boxed'

LOGIN_URL = '/accounts/login/'

LOGIN_REDIRECT_URL = '/project/'

AUTH_USER_MODEL = 'registration.User'

GOOGLE_ANALYTICS_PROPERTY_ID = 'UA-63318042-2'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false']
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        }
    }
}


CACHES = secrets.get_cache()

CACHE_MIDDLEWARE_KEY_PREFIX = 'www_mutale_cache'

CACHE_MIDDLEWARE_SECONDS = 600

CACHE_MIDDLEWARE_ALIAS = 'default'

