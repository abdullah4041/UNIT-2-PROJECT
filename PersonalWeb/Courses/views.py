from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse

# Create your views here.

def courses_view(request : HttpRequest):
    
   return render(request, "main/course.html")