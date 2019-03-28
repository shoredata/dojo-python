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
        # POST register user from form,
        # process request to register, 
        # redirect to index

    url(r'^login/$', views.login),  
        # POST login user from form,
        # process request login data, 
        # redirect to BOOKS or 
        # redirect to index

    url(r'^logout/$', views.logout), 
        # clear session data,
        # redirect to index
    
    url(r'^books/$', views.booksindex), 
        # render template after login

    url(r'^books/(?P<book_id>\d+)/showbook/$', views.booksshowbook),  
        # render template to show info for book

    url(r'^books/new/$', views.booksnew),  
        # render template to create new book review

    url(r'^books/create/$', views.bookscreate),  
        # POST new message from new review form
        # process request, 
        # redirect to valid or 
        # redirect to booksindex if error

    url(r'^books/(?P<book_id>\d+)/(?P<review_id>\d+)/destroyreview/$', views.booksdestroyreview),  
        # GET delete review from bookshow form
        # process request, 
        # redirect to bookshow
    
    url(r'^books/(?P<user_id>\d+)/showuser/$', views.booksshowuser),  
        # render template to show info for user


]


