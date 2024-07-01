from .models import Product
from django import forms

class productForms(forms.ModelForm):
    class Meta:
       model = Product
       fields = ('name','content', 'price')