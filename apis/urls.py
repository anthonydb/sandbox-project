from django.conf.urls.defaults import patterns, include, url
from apis.views import BookListAPIView, APIHomeView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^books/', BookListAPIView, name='books'),
    url(r'^$', APIHomeView.as_view()),
)