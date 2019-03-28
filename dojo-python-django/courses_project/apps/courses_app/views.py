from django.shortcuts import render, HttpResponse, redirect

from django.contrib import messages

# from time import gmtime, strftime
import datetime

# from django.utils import timezone
# from django.db import models
from .models import Course

# #################################################################
# 
# WE HAVE TO CREATE THIS FILE FROM SCRATCH EACH TIME!!!!!!!!!!!!!!!
#
# #################################################################

# urlpatterns = [
#     url(r'^$', views.index),    # GET courses, render template INDEX
#     url(r'^create/$', views.create),  # POST create new course, process new course data based on request, redirect index
#     url(r'^destroy/(?P<course_id>\d+)$', views.destroy),  
#         # GET prompt to confirm deletion of course_id, render template CONFIRM
#         # POST delete, redirect index
# ]


def index(request):
    return render(request, "courses_app/index.html", {'allcourses': Course.objects.all()})    

def create(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)

    else:
        c1 = Course.objects.create()
        c1.course_name = request.POST['course_name']
        c1.course_desc = request.POST['course_desc']
        c1.save()

    return redirect("/")

def destroy(request, course_id):
    if request.method == "GET":
        return render(request, "courses_app/confirm.html", {'course': Course.objects.get(id=course_id)})    
    elif request.method == "POST":
        Course.objects.filter(id=course_id).delete()    
    return redirect("/")
