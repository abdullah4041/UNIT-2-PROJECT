from django.urls import path
from . import views
app_name = "Project"
urlpatterns = [
    path("project/", views.project_view, name="project_view"),


]

'''path("add/", views.add_project, name="add_project"),  
    path("update/<project_id>/", views.update_project, name="update_project"),  
    path("delete/<project_id>/", views.delete_project, name="delete_project"),
'''