from django.views.generic import TemplateView
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.mail import mail_admins
import requests
import json
# from keys import *
from datetime import date
from datetime import timedelta


class APIHomeView(TemplateView):
    template_name = 'apihome.html'


def BookListAPIView(request):
    # Find a Thursday one week prior to today; the public
    # Book List API offers the list on a one-week delay.
    today = date.today()
    offset = (today.weekday() - 3) % 7
    thursday = today - timedelta(days=(offset + 7))
    date_dict = {'year': str(thursday.year),
                 'month': str(thursday.month),
                 'day': str(thursday.day)}

    # Prep and load URL.
    base_url = 'http://usatoday30.usatoday.com/api/books/'
    url = base_url + date_dict['year'] + '/' + date_dict['month'] + '/' + date_dict['day']
    r = requests.get(url)

    top_list = []
    try:
        # If JSON was returned, parse it.
        booklist = json.loads(r.text)
        for x in range(0, 20):
            books_dict = {}
            books_dict['rank'] = booklist['BookLists'][0]['BookListEntries'][x]['Rank']
            books_dict['title'] = booklist['BookLists'][0]['BookListEntries'][x]['Title']
            books_dict['author'] = booklist['BookLists'][0]['BookListEntries'][x]['Author']
            if booklist['BookLists'][0]['BookListEntries'][x]['Class'] == 'Fiction':
                books_dict['class'] = '(F)'
            elif booklist['BookLists'][0]['BookListEntries'][x]['Class'] == 'NonFiction':
                books_dict['class'] = '(NF)'
            else:
                books_dict['class'] = '(X)'
            top_list.append(books_dict)
    except ValueError:
        # Pass along a message that the API did not respond
        books_dict = {}
        books_dict['rank'] = 'The API is not responding'
        top_list.append(books_dict)
        mail_admins('Books API', 'Looks like the Books API failed.')

    return render_to_response('booklist.html',
                              {'top_list': top_list, 'date_dict': date_dict},
                              context_instance=RequestContext(request))
