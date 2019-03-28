from django.conf.urls import url
from django.urls import path, re_path
from . import views

# #################################################################
# 
# WE HAVE TO CREATE THIS FILE FROM SCRATCH EACH TIME!!!!!!!!!!!!!!!
#
# #################################################################

# /         = render INDEX.HTML
# /process/ = process data, redirect SUCCESS or INDEXw/FlashErrors
# /reset/   = clear session, redirect /
# /success/ = render SUCCESS.HTML w/home button

urlpatterns = [
    url(r'^process$', views.process), 
    url(r'^reset$', views.reset), 
    url(r'^success$', views.success), 
    url(r'^$', views.index),
    # url(r'^create/$', views.create), 
    # url(r'^(?P<number>[0-9]{2})/$', views.show),
    # url(r'^(?P<number>[0-9]{2})/edit/$', views.edit),
    # url(r'^(?P<number>[0-9]{2})/delete/$', views.destroy),
]

