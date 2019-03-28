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
        # GET list all products, render template INDEX
    url(r'^buy/$', views.buy),  
        # POST creates purchase data in db, redirect to checkout
    url(r'^checkout/$', views.checkout),  
        # GET renders checkout (has href to index)
]


