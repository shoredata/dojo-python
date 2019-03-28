from django.shortcuts import render, HttpResponse, redirect

# from time import gmtime, strftime
# import datetime
# from django.utils import timezone
# import random
# import string 

# #################################################################
# 
# WE {BASICALLY} HAVE TO CREATE THIS FILE FROM SCRATCH EACH TIME!!!!!!!!!!!!!!!
#
# #################################################################


def initsession(request):
    if "comment" not in request.session:
        request.session['comment'] = ""
        request.session['namefirst'] = ""
        request.session['namelast'] = ""
        request.session['language'] = ""
        request.session['location'] = ""
    return


def index(request):
    # show blank survey
    print("-- INDEX --")

    ### we can init our session here as necessary
    initsession(request)

    return render(request, "surveys/index.html")

def process(request):
    # process survey
    bsuccess = False
    print(request)
    if request.method == "POST":
        print("*"*50)
        initsession(request)
        print("-- Session: --")
        for key, value in request.session.items(): print('{}: {}'.format(key, value))
        print(request)
        print("-- Request: --")
        for i in request.POST: print(i +"= ", request.POST[i])

        # DO WORK HERE 
        if "ResetSurvey" in request.POST:
            if request.POST[i] == "Reset":
                print("-- RESET SURVEY --")
                request.session.clear()
                initsession(request)
        else:
            print("-- SAVE SURVEY --")
            request.session['comment'] = request.POST['comment']
            request.session['namefirst'] = request.POST['namefirst']
            request.session['namelast'] = request.POST['namelast']
            request.session['language'] = request.POST['language']
            request.session['location'] = request.POST['location']
            bsuccess = True 

        for key, value in request.session.items(): print('{}:: {}'.format(key, value))
        print("*"*50)
    if not bsuccess:
        return redirect("/")
    else:
        return redirect("/success")
        
def reset(request):
    # user requests reset, clear session and display survey
    if request.method == "POST":
        print("*"*50)
        initsession(request)
        print("Session:")
        for key, value in request.session.items(): print('{}: {}'.format(key, value))
        print(request)
        for i in request.POST: print(i +"= ", request.POST[i])

        # DO WORK HERE 
        request.session.clear()
        initsession(request)

        for key, value in request.session.items(): print('{}:: {}'.format(key, value))
        print("*"*50)
    return redirect("/")

def success(request):
    # survey response valid, display survey
    return render(request, "surveys/success.html")


# the index function is called when root is visited
# def index(request):
#     request.session['name'] = "Random Word"  # more on session below
#     if "counter" not in request.session:
#         request.session['counter'] = 0
#     for key, value in request.session.items(): print('{} => {}'.format(key, value))
#     return render(request, "random_word/index.html")

# def new(request):
#     # generate new random string
#     if request.method == "POST":
#         print("*"*50)
#         for key, value in request.session.items(): print('{} => {}'.format(key, value))
#         if "counter" not in request.session:
#             request.session['counter'] = 0
#         request.session['counter'] += 1

#         # unique_id = '%32x' % random.getrandbits(14*8)
#         allowed_chars = ''.join((string.ascii_letters, string.digits))
#         unique_id = ''.join(random.choice(allowed_chars) for _ in range(14))

#         request.session['unique_id'] = unique_id
#         for key, value in request.session.items(): print('{} => {}'.format(key, value))
#         print("*"*50)
#     return redirect("/random_word")

# def reset(request):
#     # clear counter, and clear random string
#     if request.method == "POST":
#         print("*"*50)
#         for key, value in request.session.items(): print('{} => {}'.format(key, value))
#         if "counter" not in request.session:
#             request.session['counter'] = 0
#         request.session['counter'] = 0
#         unique_id = ""  # '%32x' % random.getrandbits(14*8)
#         request.session['unique_id'] = unique_id
#         for key, value in request.session.items(): print('{} => {}'.format(key, value))
#         print("*"*50)
#     return redirect("/random_word")


