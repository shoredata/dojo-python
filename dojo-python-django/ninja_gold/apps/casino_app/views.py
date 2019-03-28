from django.shortcuts import render, HttpResponse, redirect

# from time import gmtime, strftime
# from django.utils import timezone

import datetime
import random
import string 

# #################################################################
# 
# WE HAVE TO CREATE THIS FILE FROM SCRATCH EACH TIME
#
# #################################################################


def printinfo(request, label):
    print("="*50)
    print("*** " + label + ": Request: ")
    print(request)
    for i in request.POST: 
        if type(request.POST[i]) is dict:
            for k2, v2 in request.POST[i].items(): 
                print('{}: {}'.format(k2, v2))
        else:
            print(i +": ", request.POST[i])

    # printsession also initializes session in the event it does not exist
    printsession(request, label)        
    return

def printsession(request, label):
    initsession(request) # in case it doesn't exist
    print("--- " + label + ": Session: ")
    for key, value in request.session.items(): 
        if type(value) is dict:
            for k2, v2 in value.items(): 
                print('{}: {}'.format(k2, v2))
        elif type(value) is list:
            for v in value: 
                print('{}'.format(v))
        else:
            print('{}: {}'.format(key, value))
    return

def initsession(request):
    if 'ninja' not in request.session:
        request.session['ninja'] = ""
        request.session['bank'] = 0
        request.session['action'] = ["<div style='color: black;'>" + "Initialized " + str(datetime.datetime.now()) + "</div>"]
    return


def addaction(request, somecolor, someaction):
    initsession(request)
    mywords = request.session['action']
    myword = "<div style='display:inline; color: " + somecolor + ";' width=200px>" + someaction + " " + str(datetime.datetime.now()) + "</div><br>"
    mywords.insert(0, myword)
    request.session['action'] = mywords
    print(somecolor, someaction)
    return 



def getrandomchars():
    allowed_chars = ''.join((string.printable))
    return "".join(random.choice(allowed_chars) for _ in range(32))



def index(request):
    # show session_words
    # printinfo also initializes session in the event it does not exist
    printinfo(request, "INDEX")
    return render(request, "casino_app/index.html", {'what':'Django File Upload'})

def process_money(request):
    # bsuccess = False
    # printinfo also initializes session in the event it does not exist
    printinfo(request, "PROCESS_MONEY")
    if request.method == "POST":

        bounds ={
            'farm': {'min':10, 'max':20} ,
            'cave': {'min':5, 'max':10} ,
            'house': {'min':2, 'max':5} ,
            'casino': {'min':-50, 'max':50}
        }
        bldg = request.POST['building']
        min = bounds[bldg]['min']
        max = bounds[bldg]['max']
        amount = random.randint(min,max)
        request.session['bank'] += amount

        if amount>0:
            addaction(request, "green", bldg + " you won " + str(amount) + " ")
        else:
            addaction(request, "red", bldg + " OH NO YOU LOST " + str(-1*amount) + " :( ")

        # printsession also initializes session in the event it does not exist
        printsession(request, "PROCESS_MONEY")

    return redirect("/")
        
def reset(request):
    printinfo(request, "RESET")
    if request.method == "POST":

        # DO WORK HERE 
        request.session.clear()

        # printsession also initializes session in the event it does not exist
        printsession(request, "RESET")

    return redirect("/")


def upload(request):
    if request.method == "POST":
        handle_uploaded_file(request.FILES['file'], str(request.FILES['file']))
        return HttpResponse("<h1> HOLY SHIT YOU JUST UPLOADED A FILE TO YOUR OWN PC</h1><br><p><a href='http://localhost:8000/'>GO BACK</a></p>")

    return HttpResponse("Failed")
        
def handle_uploaded_file(file, filename):
    # if not os.path.exists('upload/'):
    #     os.mkdir('upload/')
    with open('upload/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
