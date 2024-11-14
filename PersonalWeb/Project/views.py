from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Project
# Create your views here.

def project_view(request: HttpRequest):
    projects = Project.objects.all()  
    return render(request, "main/project_view.html", {'projects': projects})

'''
def add_project(request: HttpRequest):
    if request.method == "POST":
        project = Project(
        name = request.POST['name'],
        description = request.POST['description'],
        github_link = request.POST['github_link'],
        project_file = request.FILES.get('project_file'),
        )
        project.save()
        return redirect('dashboard:dashboard_view')  

    return render(request, "main/add_project.html")



def update_project(request:HttpRequest, project_id:int):
        
    project = Project.objects.get(pk=project_id)
       
    if request.method == "POST":
        
        project.name = request.POST.get('name')
        project.description = request.POST.get('description')
        project.github_link = request.POST.get('github_link')
        if 'project_file' in request.FILES:
            project.project_file = request.FILES.get('project_file')
        project.save()  
        return redirect('dashboard:dashboard_view')  
    else:
        return render(request, "main/update_project.html", {"project": project})



def delete_project(request: HttpRequest, project_id: int):
    project = Project.objects.get(pk=project_id) 
    project.project_file.delete()
    project.delete()
    return redirect('dashboard:dashboard_view')

'''