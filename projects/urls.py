from django.urls import path
from .views import ProjectHomeView, ProjectDetailView

urlpatterns=[
    path('', ProjectHomeView.as_view(), name='project_home'),
    path('<int:pk>/',ProjectDetailView.as_view(), name='project_detail'),
]