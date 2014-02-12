from django.shortcuts import render
from addsked.models import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import get_template
from django.template import Context
# Create your views here.

def create_sked(request):
    context = {}	
    if request.method == 'GET':
        books = UserSked.objects.all()
        context['get_all'] = books
    else:
        context['browse_form']= BrowseForm()

    return render_to_response('addsked.html',context,context_instance=RequestContext(request))
