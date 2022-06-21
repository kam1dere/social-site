from django.http import request
from django.shortcuts import render
from .forms import ContactForm


def contact_send(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST, request.FILES)
          

# Create your views here.
