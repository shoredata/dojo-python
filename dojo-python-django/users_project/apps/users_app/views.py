from django.shortcuts import render, HttpResponse, redirect

# from time import gmtime, strftime
import datetime

# from django.utils import timezone
# from django.db import models
from .models import User

# #################################################################
# 
# WE HAVE TO CREATE THIS FILE FROM SCRATCH EACH TIME!!!!!!!!!!!!!!!
#
# #################################################################

# urlpatterns = [
#     url(r'^$', views.index),    # GET users, template INDEX
#     url(r'^new/$', views.new),  # GET new user, data entry, template NEW
#     url(r'^(?P<user_id>\d+)/edit/$', views.edit),  # GET edit user, display & edit, template EDIT
#     url(r'^(?P<user_id>\d+)/$', views.show),  # GET show user, display only, template SHOW
#     url(r'^create/$', views.create),  # POST create new user, process new user data based on request, redirect /users/<id>
#     url(r'^(?P<user_id>\d+)/destroy/$', views.destroy),  # GET delete user data based on id, redirect /users
#     url(r'^update/$', views.update),  # POST update user data based on request, redirect /users/<id>
# ]

def index(request):
    # all_users = User.objects.all()
    # context = {'allusers': all_users}
    # return render(request, "users_app/index.html", context)    
    return render(request, "users_app/index.html", {'allusers': User.objects.all()})    

def new(request):
    print("new")
    return render(request, "users_app/new.html")    

def edit(request, user_id):
    print("edit User.id = " + str(user_id))
    return render(request, "users_app/edit.html", {'user':User.objects.get(id=user_id)})    

def show(request, user_id):
    print("show User.id = " + str(user_id))
    return render(request, "users_app/show.html", {'user':User.objects.get(id=user_id)})    

def create(request):
    print("create")
    u1 = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
    return redirect("/users/"+ str(u1.id) + "/")

def destroy(request, user_id):
    print("destroy User.id = " + str(user_id))
    User.objects.filter(id=user_id).delete()    
    return redirect("/users/")

def update(request):
    u1 = User.objects.get(id=request.POST['user_id'])
    print("update User.id = " + str(u1.id))
    u1.first_name = request.POST['first_name']
    u1.last_name = request.POST['last_name']
    u1.email = request.POST['email']
    u1.updated_at = datetime.datetime.now()
    u1.save()
    u1 = User.objects.get(id=request.POST['user_id'])
    return redirect("/users/"+ str(u1.id) + "/")
