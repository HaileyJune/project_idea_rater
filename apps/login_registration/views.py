from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import models
from .models import Users
import bcrypt

# Create your views here.
def log_reg(request):
    return render(request, 'login_registration/log_reg.html')

def reg(request):
    errors = Users.objects.register_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect ('/')

    else:
        hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = Users.objects.create(team_code= request.POST["team_code"],first_name = request.POST['fname'], last_name = request.POST['lname'], email = request.POST['email'], passhash = hash)
        request.session['userid'] = user.id       
        return redirect ('/success')

def log(request):
    errors = Users.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect ('/')
    else:
        user = Users.objects.get(email=request.POST['email'])
        request.session['userid'] = user.id
        return redirect ('/success')

def success(request):
    if 'userid' in request.session:
        return render(request, 'projects/index.html')
    else:
        return redirect('/')

def logout(request):
    request.session.clear()
    return redirect("/")