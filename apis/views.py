from django.views.generic import TemplateView
from django.template import RequestContext
from django.shortcuts import render_to_response
import requests
import json

def BookListAPIView(request):
    top_list = []
    r = requests.get('http://api.usatoday.com/open/bestsellers/books/booklists/2012/02/09/?api_key=8asfasz7segqyv5baqf66w88&encoding=json')
    booklist = json.loads(r.text)
    for x in range(0,20):
        books_dict = {}
        books_dict['rank'] = booklist['BookLists'][0]['BookListEntries'][x]['Rank']
        books_dict['title'] = booklist['BookLists'][0]['BookListEntries'][x]['Title']
        books_dict['author'] = booklist['BookLists'][0]['BookListEntries'][x]['Author']
        top_list.append(books_dict)
    return render_to_response('booklist.html', 
                            {'top_list': top_list}, 
                            context_instance=RequestContext(request))

