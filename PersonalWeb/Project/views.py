from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Project
# Create your views here.

def project_view(request: HttpRequest):
    projects = Project.objects.all()  
    return render(request, "main/project_view.html", {'projects': projects})
