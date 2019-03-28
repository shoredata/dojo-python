from django.shortcuts import render, HttpResponse, redirect

# from time import gmtime, strftime
# import datetime
# from django.utils import timezone

import random
import string 




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
    return render(request, "random_word/index.html")

def new(request):
    # generate new random string
    if request.method == "POST":
        print("*"*50)
        for key, value in request.session.items(): print('{} => {}'.format(key, value))
        if "counter" not in request.session:
            request.session['counter'] = 0
        request.session['counter'] += 1

        # unique_id = '%32x' % random.getrandbits(14*8)
        allowed_chars = ''.join((string.ascii_letters, string.digits))
        unique_id = ''.join(random.choice(allowed_chars) for _ in range(14))

        request.session['unique_id'] = unique_id
        for key, value in request.session.items(): print('{} => {}'.format(key, value))
        print("*"*50)
    return redirect("/random_word")

def reset(request):
    # clear counter, and clear random string
    if request.method == "POST":
        print("*"*50)
        for key, value in request.session.items(): print('{} => {}'.format(key, value))
        if "counter" not in request.session:
            request.session['counter'] = 0
        request.session['counter'] = 0
        unique_id = ""  # '%32x' % random.getrandbits(14*8)
        request.session['unique_id'] = unique_id
        for key, value in request.session.items(): print('{} => {}'.format(key, value))
        print("*"*50)
    return redirect("/random_word")


