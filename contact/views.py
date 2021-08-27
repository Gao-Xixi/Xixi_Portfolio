from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Contact

# Create your views here.
class ContactView(CreateView):
    model = Contact
    template_name = 'contact.html'
    fields = ['name', 'email', 'message']