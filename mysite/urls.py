# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
from django.contrib.auth import views as auth_views


admin.autodiscover()

urlpatterns = [
    url(r'^sitemap\.xml$', sitemap,
        {'sitemaps': {'cmspages': CMSSitemap}}),
]

urlpatterns += i18n_patterns(
    url(r'^admin/', include(admin.site.urls), name='admin'),  # NOQA
    url(r'^ckeditor/', include('ckeditor_uploader.urls'), name='ckeditor'),
    url(r'^project/', include('stick2uganda.urls'), name='projects'),
    # url(r'^accounts/login/', include('registration.urls')),
    url('^accounts/', include('django.contrib.auth.urls'), name='accounts'),
    url(r'^', include('cms.urls'), name='cms')  # Leave as Last
)

# This is only needed when using runserver.
if not settings.DEBUG:
    urlpatterns = [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ] + staticfiles_urlpatterns() + urlpatterns

handler404 = 'themes.views.handler404'
handler500 = 'themes.views.handler500'
