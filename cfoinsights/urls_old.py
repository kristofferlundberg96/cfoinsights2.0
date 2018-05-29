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
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy


admin.autodiscover()

urlpatterns = [
    url(r'^sitemap\.xml$', sitemap,
        {'sitemaps': {'cmspages': CMSSitemap}}),
]

prefix_urls = [
    url(r'^$', include('landing.urls')),
    url(r'^agenda/', include('agenda.urls')),
    url(r'^speakers/', include('speakers.urls')),
    url(r'^sponsors/', include('sponsors.urls')),
    url(r'^team/', include('employees.urls')),
    url(r'^survey/', include('survey.urls', namespace='survey')),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
]


urlpatterns += (
    url(r'^$', RedirectView.as_view(url=reverse_lazy('index'))),
    url(r'^denmark/', include(prefix_urls)),
    url(r'^admin/', include(admin.site.urls)),  # NOQA
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^cms', include('cms.urls')),
)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ] + staticfiles_urlpatterns() + urlpatterns
