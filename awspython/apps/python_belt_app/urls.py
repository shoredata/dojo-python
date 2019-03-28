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
        # GET render login/logout index template
    
    url(r'^register/$', views.register),  
        # POST register user from form,
        # process request to register, 
        # redirect to index if valid, 
        # redirect to index if error

    url(r'^login/$', views.login),  
        # POST login user from form,
        # process request login data, 
        # redirect to QUOTES or 
        # redirect to index

    url(r'^logout/$', views.logout), 
        # clear session data,
        # redirect to index
    
    url(r'^quotes/$', views.quotesindex), 
        # GET render quotes index template for all default routes after login

    url(r'^quotes/user/(?P<user_id>\d+)/$', views.quotesbyuser),  
        # GET render userquotes template to show quotes by user

    url(r'^quotes/myaccount/(?P<user_id>\d+)/$', views.quotesedituser),  
        # GET render editaccount template to edit user info

    url(r'^quotes/update/$', views.quotesupdateuser),  
        # POST updated user info from myaccount form
        # process request, 
        # redirect to quotes if valid or 
        # redirect to myaccount if error

    url(r'^quotes/like/$', views.quoteslike),  
        # POST like quote from quotes form
        # process request, 
        # redirect to quotes if valid or 
        # redirect to quotes if error

    url(r'^quotes/create/$', views.quotescreatequote),  
        # POST new quote from quotes form
        # process request, 
        # redirect to quotes if valid or 
        # redirect to quotes if error

    url(r'^quotes/delete/(?P<quote_id>\d+)/$', views.quotesdeletequote),  
        # delete quote for current user from quotes index
        # process request, 
        # redirect to quotes
]


