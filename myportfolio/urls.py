from django.urls import path
from .views import ProjectView, HomeView

urlpatterns=[
    path('', HomeView.as_view(), name='home'),
    path('projects/',ProjectView.as_view(), name='projects'),


    # path('contact/',ContactView.as_view(), name='project_home'),

]