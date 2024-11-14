from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard_view'),
    path("add/", views.add_project, name="add_project"),  
    path("update/<project_id>/", views.update_project, name="update_project"),  
    path("delete/<project_id>/", views.delete_project, name="delete_project"),
    path('courses/add/', views.add_course, name='add_course'),
    path('courses/update/<course_id>/', views.update_course, name='update_course'),
    path('courses/delete/<course_id>/', views.delete_course, name='delete_course'),
]