from django.urls import path
from .views import ProjectHomeView, ProjectDetailView, HomeView

urlpatterns=[
    path('', HomeView.as_view(), name='home'),
    path('projects/',ProjectHomeView.as_view(), name='projects'),


    # path('contact/',ContactView.as_view(), name='project_home'),

]