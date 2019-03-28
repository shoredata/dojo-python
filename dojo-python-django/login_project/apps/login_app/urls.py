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
    url(r'^$', views.index),   
        # render template
    url(r'^register/$', views.register),  
        # POST register user from form
        # process request to register, 
        # redirect to success or 
        # redirect to index
    url(r'^login/$', views.login),  
        # POST login user from form
        # process request login data, 
        # redirect to WALL or
        # redirect to index
    url(r'^success/$', views.success),  # GET display results
        # display template showing success of previous action

    url(r'^wall/$', views.wall), 
        # render template after login
    url(r'^logout/$', views.logout), 
        # clear session data,
        # redirect to index
    url(r'^message/new/$', views.messagenew),  
        # POST new message from form
        # process request, 
        # redirect to valid or 
        # redirect to wall if error
    url(r'^comment/new/$', views.commentnew),  
        # POST new comment from form
        # process request, 
        # redirect to valid or 
        # redirect to wall if error
    url(r'^valid/$', views.valid),
        # redirect to wall on valid comment or message
    url(r'^message/destroy/$', views.messagedestroy),  
        # POST delete message from form
        # process request, 
        # redirect to valid or 
        # redirect to wall if error
    url(r'^comment/destroy/$', views.commentdestroy),  
        # POST delete comment from form
        # process request, 
        # redirect to valid or 
        # redirect to wall if error


]


