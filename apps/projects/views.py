from django.shortcuts import render, redirect
def index(request):
    context = {
        # database stuff
    }
    return render(request, "index.html", context)

def new(request):
    # new project page
    return render(request, "new.html")

def add(request):
    # add to database
    return redirect ("/projects/" + num)

def project(reqest, num):
    context = {
        # project
    }
    return render (request, 'project.html', context)

def vote(reqest, num):
    # vote page
    return render(request, "vote.html")

def add_vote(request):
    # add vote to database
    return redirect("/projects")