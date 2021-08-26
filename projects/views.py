from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Project
# Create your views here.
class ProjectHomeView(ListView):
    model = Project
    template_name = 'projecthome.html'

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projectdetail.html'