from django.conf import urls
from addsked.views import *
urlpatterns = urls.patterns('addsked.views',  
    urls.url(r'^create/$',create_sked, name='createsked'),       
    
)
