from django.shortcuts import render, HttpResponse, redirect

# from time import gmtime, strftime
# from django.utils import timezone

import datetime
import random
import string 

# #################################################################
# 
# WE {BASICALLY} HAVE TO CREATE THIS FILE FROM SCRATCH EACH TIME!!!!!!!!!!!!!!!
#
# #################################################################


def printinfo(request, label):
    print("="*50)
    print("*** " + label + ": Request: ")
    print(request)
    for i in request.POST: print(i +": ", request.POST[i])
    # printsession also initializes session in the event it does not exist
    printsession(request, label)        
    return

def printsession(request, label):
    initsession(request) # in case it doesn't exist
    print("--- " + label + ": Session: ")
    for key, value in request.session.items(): 
        print('{}: {}'.format(key, value))
    return

def initsession(request):
    if "itemlist" not in request.session:
        request.session['itemlist'] = []        
    return

def getrandomchars():
    allowed_chars = ''.join((string.printable))
    return "".join(random.choice(allowed_chars) for _ in range(32))

def index(request):
    # show session_words
    # printinfo also initializes session in the event it does not exist
    printinfo(request, "INDEX")
    return render(request, "session_words/index.html")

def add(request):
    # bsuccess = False
    # printinfo also initializes session in the event it does not exist
    printinfo(request, "ADD")
    if request.method == "POST":
        # if amount>0:
        #     addaction("<div style='color: green;'>" + bldg + " ALL RIGHT YOU WON " + str(amount) + " ! ! (" + str(datetime.datetime.now()) + ")</div>")
        # else:
        #     addaction("<div style='color: red;'>" + bldg + " TOO BAD YOU LOST " + str(amount*-1) + " :( :( :(  (" + str(datetime.datetime.now()) + ")</div>")


        somechars = getrandomchars()
        somecolor = random.choice(["red","blue","green"])
        # DO WORK HERE 
        mywords = request.session['itemlist']
        if len(request.POST['wordtext'])>0:
            print("-- SAVE WORDS --")
            somechars = request.POST['wordtext']
            somecolor = request.POST['wordcolor']

        markedchars = "<div style='display:inline; color: " + somecolor + ";' width=200px>" + somechars + "</div><div display:inline; >" + str(datetime.datetime.now()) + "</div><br>"
        mywords.insert(0, markedchars)
        request.session['itemlist'] = mywords
        # bsuccess = True 

        # printsession also initializes session in the event it does not exist
        printsession(request, "ADD")

    return redirect("/session_words")
        
def clear(request):
    printinfo(request, "CLEAR")
    if request.method == "POST":

        # DO WORK HERE 
        request.session.clear()

        # printsession also initializes session in the event it does not exist
        printsession(request, "ADD")

    return redirect("/session_words")


