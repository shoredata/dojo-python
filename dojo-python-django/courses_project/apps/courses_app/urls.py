from django.conf.urls import url
from django.urls import path, re_path
from . import views

# #################################################################
# 
# WE HAVE TO CREATE THIS FILE FROM SCRATCH EACH TIME!!!!!!!!!!!!!!!
#
# #################################################################

# Notice that for every form submission we use a POST method, while we're rendering our templates from get routes.

urlpatterns = [
    url(r'^$', views.index),    # GET courses, render template INDEX
    url(r'^create/$', views.create),  # POST create new course, process new course data based on request, redirect index
    url(r'^destroy/(?P<course_id>\d+)/$', views.destroy),  
        # GET prompt to confirm deletion of course_id, render template CONFIRM
        # POST delete, redirect index
]


