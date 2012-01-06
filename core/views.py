#from django.shortcuts import render_to_response
from django.views.generic import TemplateView

#def home(request):
#    return render_to_response('home.html')

class HomePageView(TemplateView):
    template_name = "home.html"
