from django.shortcuts import render,redirect
from Project.models import Project
from Courses.models import Course
from django.http import HttpRequest,HttpResponse

# Create your views here.


def dashboard_view(request: HttpRequest):
    projects = Project.objects.all()  
    courses = Course.objects.all()  
    
    context = {
        'projects': projects,
        'courses': courses
    }
    return render(request, "main/dashboard.html", context)


def project_view(request: HttpRequest):
    projects = Project.objects.all()  
    return render(request, "main/project_view.html", {'projects': projects})


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




def add_course(request: HttpRequest):
    if request.method == "POST":
        new_course = Course(
        name = request.POST['name'],
        academy = request.POST['academy'],
        description = request.POST['description'],
        start_date = request.POST['start_date'],
        end_date = request.POST['end_date'],
        certificate_image = request.FILES.get('certificate_image'), 
        )
        new_course.save()
        
        return redirect('dashboard:dashboard_view')

    return render(request, "main/add_course.html")


def update_course(request: HttpRequest, course_id: int):
    course = Course.objects.get(id=course_id)

    if request.method == "POST":
        course.name = request.POST.get('name')
        course.academy = request.POST.get('academy')
        course.description = request.POST.get('description')
        course.start_date = request.POST.get('start_date')
        course.end_date = request.POST.get('end_date')

        if request.FILES.get('certificate_image'):
            course.certificate_image = request.FILES.get('certificate_image')

        course.save()

        return redirect('dashboard:dashboard_view')

    return render(request, "main/update_course.html", {'course': course})


def delete_course(request: HttpRequest, course_id: int):
    course = Course.objects.get(id=course_id)
    course.certificate_image.delete()
    course.delete()
    return redirect('dashboard:dashboard_view')
