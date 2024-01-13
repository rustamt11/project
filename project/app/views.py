from django.shortcuts import render, get_object_or_404
from .models import Project

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'product_detail.html', {'project': project})


def project_list(request):
    projects = Project.objects.all()  # Query all projects from the database
    return render(request, 'product_list.html', {'projects': projects})
