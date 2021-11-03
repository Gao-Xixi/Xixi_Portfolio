from datetime import datetime

from django.db import models
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, CreateView

from .forms import ContactForm
from .models import Contact
# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'
class ProjectView(TemplateView):
    template_name = 'projects.html'

class ContactView(CreateView):
    model = Contact
    template_name = 'contact.html'
    form_class = ContactForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post_date = datetime.now()
        form.save()
        return super(CreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('home')
