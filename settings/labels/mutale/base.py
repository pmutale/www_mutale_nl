# -*- coding: utf-8 -*-
from settings.core import *
import psycopg2
import urlparse
import dj_database_url
from django.utils.translation import ugettext_lazy as _

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'mysite', 'static'),
    os.path.join(BASE_DIR, 'themes', 'static'),
    os.path.join(BASE_DIR, 'stick2uganda', 'static'),
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
                'cms.context_processors.cms_settings'
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
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
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
    # 'djangocms_link',
    # 'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    # 'cmsplugin_filer_image',
    'cmsplugin_filer_utils',
    # 'djangocms_style',
    'djangocms_snippet',
    'djangocms_googlemap',
    # 'djangocms_video',
    'mptt',

    #  Apps
    'mysite',
    'themes',
    'stick2uganda',
)

LANGUAGES = (
    ('en', 'English'),
    ('nl', 'Nederlands'),
    ('sw', 'Swahili'),
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

DATABASE_URL = 'postgres://oogcsuzgfwhqbc:0da4b0d51b2f508e4c00308e3c583c2dd9999b6b439a5501dcd643602b455167@ec2-54' \
               '-247-92-185.eu-west-1.compute.amazonaws.com:5432/dmtkic08buj90'

DATABASES = {
    'default':
        dj_database_url.config(default=DATABASE_URL)
}

MIGRATION_MODULES = {

}

# CMS_TOOLBAR_ANONYMOUS_ON = False

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

DATE_INPUT_FORMATS = '%Y/%m/%d'

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

WSGI_APPLICATION = 'mysite.wsgi.application'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

DEFAULT_FROM_EMAIL = 'webmaster@mutale.nl'

LOGIN_URL = '/accounts/login/'

AUTH_USER_MODEL = 'registration.User'

