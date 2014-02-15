from django import forms
from django.forms import ModelForm
from addsked.models import *
class CreateSkedForm(forms.ModelForm):
    class Meta:
        model = UserSked
        fields = '__all__'



   


   
