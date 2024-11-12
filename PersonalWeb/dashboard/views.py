from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse

# Create your views here.

def dashboard_view(request : HttpRequest):
    
   return render(request, "main/dashboard.html")