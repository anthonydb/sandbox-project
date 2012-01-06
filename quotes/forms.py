from django.template import RequestContext
from quotes.models import Submission, Quote
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django import forms
from django.forms import ModelForm, Textarea

# Suggest-a-quote form

class SuggestForm(ModelForm):
    item = forms.CharField(label='Quote', 
                           widget=Textarea(attrs={'cols': 60, 'rows': 10})
                           )
    source = forms.CharField(label='Source', 
                           widget=Textarea(attrs={'cols': 60, 'rows': 5})
                           )
    class Meta:
        model = Submission
        exclude = ['date']

def submit_quote(request):
    if request.method == 'POST':
        form = SuggestForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/quotes/suggest/thanks/')
    else:
        form = SuggestForm()
    return render_to_response('suggest.html',
                                { 'form': form },
                                context_instance=RequestContext(request))

# Search quotes form

class SearchForm(ModelForm):
    quote = forms.CharField(label='Term',
                            widget=Textarea(attrs={'cols': 40, 'rows': 1})
                           )
    class Meta:
        model = Quote
        exclude = ['source', 'author', 'categories', 'slug']


def search_quotes(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            term = form.cleaned_data['quote']
            results = Quote.objects.filter(quote__contains=term).order_by('quote')
            if not results:
                results = ['None']
            return render_to_response('search.html',
                                        { 'form': form, 'results_list': results },
                                        context_instance=RequestContext(request))
    else:
        form = SearchForm()
    return render_to_response('search.html',
                             { 'form': form },
                             context_instance=RequestContext(request))

