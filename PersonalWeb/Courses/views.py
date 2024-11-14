from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Course
# Create your views here.

def courses_view(request : HttpRequest):
   courses = Course.objects.all()
   return render(request, "main/course.html", {'courses': courses})

