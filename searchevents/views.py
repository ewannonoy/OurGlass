from django.shortcuts import render
from addsked.models import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import get_template
from django.template import Context
# Create your views here.

def search_sked(request):
    context = {}	
    if request.method == 'GET':
        books = UserSked.objects.all()
        context['get_all'] = books
   
    return render_to_response('searchevents.html',context,context_instance=RequestContext(request))

def open_sked(request, query):
    context = {}	
    if request.method == 'GET':
        books = UserSked.objects.all()
        context['get_all'] = books
   
    return render_to_response('searchevents.html',context,context_instance=RequestContext(request))
