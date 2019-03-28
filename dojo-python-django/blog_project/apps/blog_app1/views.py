from django.shortcuts import render, HttpResponse, redirect

# #################################################################
# 
# WE {BASICALLY} HAVE TO CREATE THIS FILE FROM SCRATCH EACH TIME!!!!!!!!!!!!!!!
#
# #################################################################


# blog_app1 = test app
# / - display test1.html (test was stripped off by project urls.py)

# the index function is called when root is visited
def index(request):
    # display test html from platform
    context = {
        "email" : "blog@gmail.com",
        "name" : "mike"
    }
    return render(request, "blog_app1/test1.html", context)

