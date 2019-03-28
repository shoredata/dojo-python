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


urlpatterns = [
    url(r'^$', views.index),
    path('articles/2003/', views.show),
    # re_path(r'^articles/(?P\d+)$', views.month_archive),
    re_path(r'^bio/(?P<username>\w+)/$', views.month_archive, name='bio'),
    # path('login/<int:year>/<int:month>/<int:day>/$', views.get_date),
    re_path(r'^login/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.get_date),
]

