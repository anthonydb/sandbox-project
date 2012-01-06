from django.conf.urls.defaults import *
#from core.views import home
from core.views import HomePageView

urlpatterns = patterns('',
#    url(r'^$', home, name='home'),
    (r'^$', HomePageView.as_view()),
)
