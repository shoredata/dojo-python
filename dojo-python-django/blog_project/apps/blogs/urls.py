from django.conf.urls import url
from django.urls import path, re_path
from . import views

# #################################################################
# 
# WE HAVE TO CREATE THIS FILE FROM SCRATCH EACH TIME!!!!!!!!!!!!!!!
#
# #################################################################

# blogs app
# / - display "placeholder to later display all the list of blogs" 
#     via HttpResponse. Have this be handled by a method named 'index'.
# /new - display "placeholder to display a new form to create a new blog" 
#     via HttpResponse. Have this be handled by a method named 'new'.
# /create - Have this be handled by a method named 'create'.  
#     For now, have this url redirect to /.
# /{{number}} - display 'placeholder to display blog {{number}}'.  
#     For example /15 should display a message 'placeholder to display blog 15'.  
#     Have this be handled by a method named 'show'.
# /{{number}}/edit - display 'placeholder to edit blog {{number}}.  
#     Have this be handled by a method named 'edit'.
# /{{number}}/delete - 
#     Have this be handled by a method named 'destroy'. 
#     For now, have this url redirect to /. 
#
# Have the root route (e.g. localhost/) be handled by the index method in the blogs' view file.


urlpatterns = [
    url(r'^$', views.index),
    url(r'^new/$', views.new), 
    url(r'^create/$', views.create), 
    url(r'^books/$', views.index2), 
    url(r'^(?P<number>[0-9]{2})/$', views.show),
    url(r'^(?P<number>[0-9]{2})/edit/$', views.edit),
    url(r'^(?P<number>[0-9]{2})/delete/$', views.destroy),
]

