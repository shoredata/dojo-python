from django.conf.urls import url
from django.urls import path, re_path
from . import views

# #################################################################
# 
# WE HAVE TO CREATE THIS FILE FROM SCRATCH EACH TIME!!!!!!!!!!!!!!!
#
# #################################################################

# for random_word the main urls.py will have stripped everythiong off and here we are until we get new

urlpatterns = [
    url(r'^$', views.index),
    
    # url(r'^new/$', views.new), 
    # url(r'^reset/$', views.reset), 

    # url(r'^create/$', views.create), 
    # url(r'^(?P<number>[0-9]{2})/$', views.show),
    # url(r'^(?P<number>[0-9]{2})/edit/$', views.edit),
    # url(r'^(?P<number>[0-9]{2})/delete/$', views.destroy),
]
