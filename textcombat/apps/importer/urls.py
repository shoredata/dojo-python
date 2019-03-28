from django.conf.urls import url
from django.urls import path, re_path
from . import views

# #################################################################
# 
# WE HAVE TO CREATE THIS FILE FROM SCRATCH EACH TIME
#
# #################################################################

# Notice that for every form submission we use a POST method
# while we're rendering our templates from get routes.

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
    

    url(r'^main/$', views.mainindex), 
        # GET render main page after login


    url(r'^accounts/$', views.accounts), 
        # GET render accounts list page

    url(r'^accounts/deliver/$', views.randdelivery), 
        # GET autogenerate a random delivery now() for random acct_id
    url(r'^accounts/(?P<account_id>\d+)/deliver/$', views.randaccountdelivery), 
        # GET autogenerate a random delivery now() for acct_id
    url(r'^trucks/(?P<truck_id>\d+)/deliver/$', views.randtruckdelivery), 
        # GET autogenerate a random delivery now() for acct_id


    url(r'^account/(?P<account_id>\d+)/view/$', views.viewaccount), 
        # GET render account details page


    url(r'^trucks/$', views.trucks), 
        # GET render trucks list page

    url(r'^truck/(?P<truck_id>\d+)/view/$', views.viewtruck), 
        # GET render truck details page



    url(r'^deliveries/$', views.deliveries), 
        # GET render deliveries list page

    url(r'^deliveries/map/$', views.deliveriesmap), 
        # GET render deliveries map page

    url(r'^deliveries/(?P<truck_id>\d+)/truck/map/$', views.truckdeliveriesmap), 
        # GET render deliveries map page

    url(r'^deliveries/(?P<account_id>\d+)/account/map/$', views.accountdeliveriesmap), 
        # GET render deliveries map page

    url(r'^deliveries/(?P<delivery_id>\d+)/delivery/map/$', views.deliverymap), 
        # GET render deliveries map page

    url(r'^delivery/(?P<delivery_id>\d+)/view/$', views.viewdelivery), 
        # GET render delivery details page

    url(r'^account/(?P<account_id>\d+)/map/$', views.accountmap), 
        # GET render deliveries map page


    url(r'^myaccount/(?P<user_id>\d+)/edit/$', views.edituser),  
        # GET render edit template for current user

    url(r'^myaccount/update/$', views.updateuser),  
        # POST update user data from form
        # process request, 
        # redirect to myaccount if valid or 
        # redirect to myaccount if error


    url(r'^import/$', views.importselect),  
        # GET render import data page

    url(r'^import/upload/$', views.importupload),  
        # POST create new import from POST data from form
        # process request, 
        # redirect to main if valid or 
        # redirect to import if error


]


