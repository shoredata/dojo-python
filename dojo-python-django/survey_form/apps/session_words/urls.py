from django.conf.urls import url
from django.urls import path, re_path
from . import views

# #################################################################
# 
# WE HAVE TO CREATE THIS FILE FROM SCRATCH EACH TIME!!!!!!!!!!!!!!!
#
# #################################################################

# /           = render INDEX.HTML
# /add_word/  = process data, redirect SUCCESS or INDEXw/FlashErrors
# /clear/     = clear session, redirect
# /success/   = redirect

urlpatterns = [
    url(r'^add_word$', views.add), 
    url(r'^clear$', views.clear), 
    url(r'^$', views.index),
    # url(r'^create/$', views.create), 
    # url(r'^(?P<number>[0-9]{2})/$', views.show),
    # url(r'^(?P<number>[0-9]{2})/edit/$', views.edit),
    # url(r'^(?P<number>[0-9]{2})/delete/$', views.destroy),
]

