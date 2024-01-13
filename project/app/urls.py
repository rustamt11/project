from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.project_detail, name='project_detail'),
    path('projects/', views.project_list, name='project_list'),
]
