from django.shortcuts import render, HttpResponse, redirect

from time import gmtime, strftime
import datetime

from django.utils import timezone
# from django.db import models
from apps.blogs.models import Author

# #################################################################
# 
# WE {BASICALLY} HAVE TO CREATE THIS FILE FROM SCRATCH EACH TIME!!!!!!!!!!!!!!!
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


# the index function is called when root is visited
def index(request):
    # response = "placeholder to later display all the list of blogs"
    # return HttpResponse(response)
    # request.session['name'] = "BLOGS"  # more on session below
    mytime = "ABCD"
    now = timezone.now()
    mytime = strftime("%Y-%m-%d %H:%M %p", gmtime())
    # snow = datetime.datetime.utcnow().replace(tzinfo=now)
    # print(snow)
    context = {'currenttime':mytime}
    return render(request, "blogs/index.html", context)

def index2(request):
    context = {"authors": Author.objects.all()}
    return render(request, "books/index2.html", context)

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)    

def create(request):
    if request.method == "POST":
        print("*"*50)
        print(request)
        for i in request.POST:
            print(i +":", request.POST[i])
        # print(request.POST)
        # print(request.POST['name'])
        # print(request.POST['desc'])
        request.session['name'] = "Test"  # more on session below
        print("*"*50)
        return redirect("/")
    else:
        return redirect("/")
    # return redirect("/blogs")        

def show(request, number):
    response = "placeholder to display blog " + str(number)
    return HttpResponse(response)

def edit(request, number):
    response = "placeholder to edit blog " + str(number)
    return HttpResponse(response)        

def destroy(request, number):
    return redirect("/blogs")        
