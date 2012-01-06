from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^quotes/', include('quotes.urls')),
    (r'^$', include('core.urls.home')),
)
