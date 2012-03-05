from django.views.generic import TemplateView
from django.template import RequestContext
from django.shortcuts import render_to_response
import requests
import json
from keys import *
from datetime import date
from datetime import timedelta

class APIHomeView(TemplateView):
    template_name = 'apihome.html'

def BookListAPIView(request):
    # Find a Thursday two weeks prior to today; the Book List API does not offer the latest list.
    today = date.today()
    offset = (today.weekday() - 3) % 7
    thursday = today - timedelta(days=(offset+14))
    date_dict = {'year': str(thursday.year), 'month': str(thursday.month), 'day': str(thursday.day)}
    
    # prep and load URL
    base_url = 'http://api.usatoday.com/open/bestsellers/books/booklists/' 
    url = base_url + date_dict['year'] + '/' + date_dict['month'] + '/' + date_dict['day'] + '/?api_key=' + BOOK_KEY + '&encoding=json'
    r = requests.get(url)
    booklist = json.loads(r.text)

    #parse the JSON returned by the API
    top_list = []
    for x in range(0,20):
        books_dict = {}
        books_dict['rank'] = booklist['BookLists'][0]['BookListEntries'][x]['Rank']
        books_dict['title'] = booklist['BookLists'][0]['BookListEntries'][x]['Title']
        books_dict['author'] = booklist['BookLists'][0]['BookListEntries'][x]['Author']
        top_list.append(books_dict)

    return render_to_response('booklist.html', 
                            {'top_list': top_list, 'date_dict': date_dict}, 
                            context_instance=RequestContext(request))

