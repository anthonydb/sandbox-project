from django.views.generic import TemplateView
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.mail import mail_admins
import requests
from .keys import *
from datetime import date


class APIHomeView(TemplateView):
    template_name = 'apihome.html'


def BookListAPIView(request):
    # Construct API url
    api_key = nyt_api
    base_url = 'https://api.nytimes.com/svc/books/v3/lists.json'
    payload = {'api-key': api_key,
               'list': 'combined-print-and-e-book-nonfiction'}

    # Attempt to fetch the API and build a list of titles
    try:
        r = requests.get(base_url, params=payload)
        nyt_list_response = r.json()
        nyt_list_date = nyt_list_response['results'][0]['bestsellers_date']

        # A list of dicts for titles
        top_list = []

        for book in nyt_list_response['results']:
            books_dict = {}
            books_dict['rank'] = str(book['rank'])
            books_dict['title'] = book['book_details'][0]['title']
            books_dict['author'] = book['book_details'][0]['author']
            books_dict['amazon_link'] = book['amazon_product_url']
            top_list.append(books_dict)

    except ValueError:
        # Pass along a message that the API did not respond
        books_dict = {}
        books_dict['rank'] = 'The API is not responding'
        top_list.append(books_dict)
        mail_admins('Books API', 'Looks like the Books API failed.')

    return render_to_response('booklist.html',
                              {'top_list': top_list, 'list_date': nyt_list_date},
                              context_instance=RequestContext(request))
