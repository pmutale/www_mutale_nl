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
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = [
    url(r'^sitemap\.xml$', sitemap,
        {'sitemaps': {'cmspages': CMSSitemap}}),
]
# Rosetta
if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += i18n_patterns(
        url(r'^rosetta/', include('rosetta.urls')),
    )

# Others
urlpatterns += i18n_patterns(
    url(r'^admin/', include(admin.site.urls)),  # NOQA
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^project/', include('stick2uganda.urls')),
    # url(r'^accounts/login/', include('registration.urls')),
    url('^accounts/', include('django.contrib.auth.urls')),
    url(r'^', include('cms.urls'))  # Leave as Last
)

# Statics
urlpatterns += i18n_patterns(
    url(r'^media/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
) + staticfiles_urlpatterns() + urlpatterns

#     urlpatterns += staticfiles_urlpatterns()
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'themes.views.handler404'
handler500 = 'themes.views.handler500'

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
