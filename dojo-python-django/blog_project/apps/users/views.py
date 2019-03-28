from django.shortcuts import render, HttpResponse, redirect

# #################################################################
# 
# WE {BASICALLY} HAVE TO CREATE THIS FILE FROM SCRATCH EACH TIME!!!!!!!!!!!!!!!
#
# #################################################################

# users app
# /register - display 'placeholder for users to create a new user record'
#   register
# /login - display 'placeholder for users to login' 
#   login
# /users/new - have the same method that handles /register also handle the url request of /users/new
#   register
# /users - display 'placeholder to later display all the list of users'
#   show_all

# the index function is called when root is visited
def register(request):
    response = "placeholder for users to create a new user record"
    return HttpResponse(response)

def login(request):
    response = "placeholder for users to login"
    return HttpResponse(response)    

def show_all(request):
    response = "placeholder to later display all the list of users"
    return HttpResponse(response)    

