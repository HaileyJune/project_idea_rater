from django.shortcuts import render, redirect
from django.contrib import messages
from apps.login_registration.models import Users
from apps.projects.models import Project, Reviews

def index(request):
    context = {
        "projects": Project.objects.all()
    }
    return render(request, "projects/index.html", context)

def project(request, id):
    context = {
        "this_project": Project.objects.get(id=id)
    }
    return render (request, 'project.html', context)

def new(request):
    return render(request, "projects/new.html")

def edit(request, id):
    
    return render(request, "edit.html")

def update(request, id):
    # add changes to project
    return redirect("/projects")

def add_vote(request, id):
    
    # add vote to database
    return redirect("/projects")