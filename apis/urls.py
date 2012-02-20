from django.conf.urls.defaults import patterns, include, url
from apis.views import BookListAPIView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^books/', BookListAPIView, name='books'),
)
