from django.conf.urls import url
from django.urls import path, re_path
from . import views

# #################################################################
# 
# WE HAVE TO CREATE THIS FILE FROM SCRATCH EACH TIME
#
# #################################################################

# /               = render INDEX.HTML
# /process_money/ = process data, redirect to INDEX
# /reset/         = process clear, redirect to INDEX

urlpatterns = [
    url(r'^process_money$', views.process_money), 
    url(r'^reset$', views.reset), 
    url(r'^upload$', views.upload),
    url(r'^$', views.index),
    # url(r'^upload$', views.upload, name="upload"),

    # url(r'^create/$', views.create), 
    # url(r'^(?P<number>[0-9]{2})/$', views.show),
    # url(r'^(?P<number>[0-9]{2})/edit/$', views.edit),
    # url(r'^(?P<number>[0-9]{2})/delete/$', views.destroy),
]



