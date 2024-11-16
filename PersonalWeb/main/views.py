from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from Project.models import Project
from Courses.models import Course
# Create your views here.

def home(request : HttpRequest):
   projects = Project.objects.all()  
   courses = Course.objects.all()  

   context = {
      'projects': projects,
      'courses': courses
   }
   return render(request, "main/home.html", context)
