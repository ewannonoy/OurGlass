from django.conf import urls
from searchevents.views import *
urlpatterns = urls.patterns('searchevents.views',  
    urls.url(r'^search/$',search_sked, name='searchesked'),
    urls.url(r'^opensked$', open_sked, name='opensked'),     
    
)
