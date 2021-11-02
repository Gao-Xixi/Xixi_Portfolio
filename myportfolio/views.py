from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Contact
# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'
class ProjectView(TemplateView):
    template_name = 'projects.html'

# class ContactView()