from django.views.generic import TemplateView
from django.template import RequestContext
from django.shortcuts import render
from .api import fetch_nyt_booklist


class BooklistHomeView(TemplateView):
    template_name = 'booklist_home.html'

def BookListNonfictionView(request):
    nyt_list_date, top_list = fetch_nyt_booklist('combined-print-and-e-book-nonfiction')

    return render(request,
                  'nonfiction_list.html',
                  {'top_list': top_list,
                   'list_date': nyt_list_date})

def BookListFictionView(request):
    nyt_list_date, top_list = fetch_nyt_booklist('combined-print-and-e-book-fiction')

    return render(request,
                  'fiction_list.html',
                  {'top_list': top_list,
                   'list_date': nyt_list_date})
