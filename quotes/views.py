from django.views.generic import DetailView, ListView, TemplateView
from django.template import RequestContext
from quotes.models import Quote, Author, Categories
from django.shortcuts import get_object_or_404, render_to_response
from random import randint
from django.db.models import Count

# Home page featuring a random quote
#class QuotesHomeView(ListView):
#    model = Quote
#    template_name = 'quotes_home.html'
#    queryset = Quote.random.pull_random_quote()
#    context_object_name = 'random_quote'

#Home page featuring a random quote
def QuotesHomeView(request):
    count = Quote.objects.all().aggregate(count=Count('id'))['count']
    random_index = randint(0, count -1)
    random_quote = Quote.objects.all()[random_index]     
    return render_to_response('quotes_home.html',
                            { 'random_quote': random_quote },
                            context_instance=RequestContext(request))

# Quote list
class QuotesListView(ListView):
    template_name = 'quotes_list.html'
    queryset = Quote.objects.order_by('quote')
    context_object_name = 'quotes_list'

# Quote detail
def QuotesDetailView(request, quoteslug):
    quote = get_object_or_404(Quote, slug=quoteslug)   
    return render_to_response('quotes_detail.html',
                            { 'quote' : quote }, 
                            context_instance=RequestContext(request))

# Author list
class AuthorListView(ListView):
    template_name = 'author_list.html'
    queryset = Author.objects.order_by('lastname')
    context_object_name = 'authors_list'

# Quotes by author
def AuthorQuotesView(request, authorslug):
    author = get_object_or_404(Author, slug__iexact=authorslug)
    author_quote_list = Quote.objects.filter(author=author)

    return render_to_response('author_quote_list.html', 
                            { 'author_quote_list' : author_quote_list }, 
                            context_instance=RequestContext(request))

#Categories views

class CategoriesListView(ListView):
    template_name = 'categories_list.html'
    queryset = Categories.objects.order_by('category')
    context_object_name = 'categories_list'

def CategoriesQuotesView(request, categoryslug):
    category = get_object_or_404(Categories, slug__iexact=categoryslug)
    categories_quote_list = Quote.objects.filter(categories=category).order_by('author')
    category_name = Categories.objects.filter(slug=categoryslug)
    return render_to_response('categories_quote_list.html',
                            { 'categories_quote_list' : categories_quote_list,
                              'categories' : category_name },
                            context_instance=RequestContext(request))

# Submit thanks

class submit_thanks(TemplateView):
    template_name = 'suggest_thanks.html'

# About

class AboutPageView(TemplateView):
    template_name = 'about.html'
