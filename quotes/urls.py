from django.urls import path, re_path
from quotes.views import QuotesHomeView, QuotesDetailView, AuthorListView, AuthorQuotesView, CategoriesListView, CategoriesQuotesView, submit_thanks, AboutPageView
from quotes.forms import submit_quote, search_quotes

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    re_path(r'authors/(?P<authorslug>[-\w]+)/', AuthorQuotesView, name='author_quotes'),
    re_path(r'^authors/', AuthorListView.as_view(), name='authors'),
    re_path(r'^categories/(?P<categoryslug>[-\w]+)/', CategoriesQuotesView, name='category_quotes'),
    re_path(r'^categories/', CategoriesListView.as_view(), name='categories'),
    re_path(r'^search/', search_quotes, name='search'),
    re_path(r'^suggest/thanks/', submit_thanks.as_view(), name='thanks'),
    re_path(r'^suggest/', submit_quote, name='suggest'),
    re_path(r'^about/', AboutPageView.as_view(), name='about'),
    re_path(r'^(?P<quoteslug>[-\w]+)/', QuotesDetailView, name='quote_detail'),
    path('', QuotesHomeView, name='home')
]
