from django.shortcuts import render

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import get_template
from django.template import Context
from addsked.models import *
from datetime import date
from addsked.forms import *
# Create your views here.

def create_sked(request):
    context = {}	
    if request.method == 'GET':
        context['create_form'] = CreateSkedForm()

    elif request.method == 'POST':
        skedValues = CreateSkedForm(request.POST, request.FILES)
        context['create_form'] = CreateSkedForm()

        if skedValues.is_valid():
            skedValues = skedValues.save(commit=False)            
            skedValues.ratings = 0
            skedValues.likes = 0
            skedValues.date_created=date.today()
            skedValues.save()

        else:
            print 'Oops! There is an error!!!!!'
            context['create_form']=skedValues
            
            
    return render_to_response('addsked.html',context,context_instance=RequestContext(request))
