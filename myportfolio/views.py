from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Project
# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'
class ProjectHomeView(ListView):
    model = Project
    template_name = 'projects.html'

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projectdetail.html'
# class ContactView()