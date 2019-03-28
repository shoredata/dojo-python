from django.shortcuts import render, HttpResponse, redirect

# from time import gmtime, strftime
# import datetime
# from django.utils import timezone

import random
import string 

# from .models import user




# #################################################################
# 
# WE {BASICALLY} HAVE TO CREATE THIS FILE FROM SCRATCH EACH TIME!!!!!!!!!!!!!!!
#
# #################################################################

# create and display 14-digit random string, allow NEW and RESET

# the index function is called when root is visited
def index(request):
    request.session['name'] = "Random Word"  # more on session below
    if "counter" not in request.session:
        request.session['counter'] = 0
    for key, value in request.session.items(): print('{} => {}'.format(key, value))
    return render(request, "books/index.html")