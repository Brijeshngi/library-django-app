from socket import fromshare
from django.core import validators
from django import forms
from .models import bookDetails

class BookAddition(forms.ModelForm):
    class Meta:
        model = bookDetails
        fields = ['name', 'author', 'ISBN'] 

