from django.shortcuts import render, HttpResponse, redirect

# #################################################################
# 
# WE {BASICALLY} HAVE TO CREATE THIS FILE FROM SCRATCH EACH TIME!!!!!!!!!!!!!!!
#
# #################################################################


# surveys app
# /surveys - display "placeholder to display all the surveys created"
#   def:index
# /surveys/new - display "placeholder for users to add a new survey"
#   def:new


# the index function is called when root is visited
def index(request):
    response = "placeholder to display all the surveys created"
    return HttpResponse(response)

def new(request):
    response = "placeholder for users to add a new survey"
    return HttpResponse(response)    

