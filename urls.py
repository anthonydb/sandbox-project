from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^words/', include('quotes.urls')),
    url(r'^apis/', include('apis.urls')),
#ll
    (r'^$', include('core.urls.home')),
)
