from django.urls import path
from . import views

app_name = "Courses"

urlpatterns = [
    path("courses/", views.courses_view, name="courses_view"), 
]