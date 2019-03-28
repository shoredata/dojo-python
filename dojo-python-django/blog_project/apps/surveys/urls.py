from django.conf.urls import url
from django.urls import path, re_path
from . import views

# #################################################################
# 
# WE HAVE TO CREATE THIS FILE FROM SCRATCH EACH TIME!!!!!!!!!!!!!!!
#
# #################################################################

# surveys app
# /surveys - display "placeholder to display all the surveys created"
#   def:index
# /surveys/new - display "placeholder for users to add a new survey"
#   def:new

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new/$', views.new), 
]

