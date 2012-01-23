from django.conf.urls.defaults import patterns, include, url
from quotes.views import QuotesListView, QuotesHomeView, QuotesDetailView, AuthorListView, AuthorQuotesView, CategoriesListView, CategoriesQuotesView, submit_thanks, AboutPageView
from quotes.forms import submit_quote, search_quotes

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^list/', QuotesListView.as_view()),
    url(r'^authors/(?P<authorslug>[-\w]+)/', AuthorQuotesView),
    url(r'^authors/', AuthorListView.as_view(), name='authors'),    
    url(r'^categories/(?P<categoryslug>[-\w]+)/', CategoriesQuotesView),
    url(r'^categories/', CategoriesListView.as_view(), name='categories'),
    url(r'^search/', search_quotes, name='search'),
    url(r'^suggest/thanks/', submit_thanks.as_view(), name='thanks'),
    url(r'^suggest/', submit_quote, name='suggest'),
    url(r'^about/', AboutPageView.as_view(), name='about'),
    url(r'^(?P<quoteslug>[-\w]+)/', QuotesDetailView),
#    url(r'^$', QuotesHomeView.as_view(), name='home'),
    url(r'^$', QuotesHomeView, name='home'),
)
