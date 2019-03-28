from django.conf.urls import url
from django.urls import path, re_path
from . import views

# #################################################################
# 
# WE HAVE TO CREATE THIS FILE FROM SCRATCH EACH TIME!!!!!!!!!!!!!!!
#
# #################################################################

# users app
# /register - display 'placeholder for users to create a new user record'
#   register
# /login - display 'placeholder for users to login' 
#   login
# /users/new - have the same method that handles /register also handle the url request of /users/new
#   register
# /users - display 'placeholder to later display all the list of users'
#   show_all

urlpatterns = [
    url(r'^register/$', views.register),
    url(r'^login/$', views.login), 
    url(r'^new/$', views.register),
    url(r'^$', views.show_all), 
]

