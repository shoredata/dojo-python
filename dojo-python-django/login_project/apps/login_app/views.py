from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

# from time import gmtime, strftime
# import datetime
import bcrypt

# from django.utils import timezone
# from django.db import models
from .models import User
from .models import Message
from .models import Comment

# #################################################################
# 
# WE HAVE TO CREATE THIS FILE FROM SCRATCH EACH TIME!!!!!!!!!!!!!!!
#
# #################################################################


def initsession(request):
    if 'successmessage' not in request.session:
        request.session['successmessage'] = ""

        request.session['login_userid'] = 0
        # request.session['login_email'] = ""
        # request.session['login_passwordhash'] = ""

        # request.session['firstname'] = ""
        # request.session['lastname'] = ""
        # request.session['email'] = ""
        # request.session['password1'] = ""
        # request.session['password2'] = ""
    return


def index(request):
    initsession(request)
    print("index")
    return render(request, "login_app/index.html", {'allusers': User.objects.all()})    

def register(request):
    print("register")
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors):
            print(errors)
            for key in errors:
                print(key,errors[key])
                messages.error(request, key + ":" + errors[key])
        else:
            if request.POST['password1'] != request.POST['password2']:
                messages.add_message(request, messages.ERROR, "Passwords do not match")
        if len(errors)==0:
            if User.objects.filter(email=request.POST['email']).exists():
                messages.add_message(request, messages.ERROR, "Email address already exists in database")
            else:
                mypassword = request.POST['password1'].encode()
                mypasswordhash = bcrypt.hashpw(mypassword, bcrypt.gensalt())
                if bcrypt.checkpw(mypassword, mypasswordhash):
                    print("New Password Verfied, storing ..")
                    u1 = User.objects.create(
                        firstname=request.POST['firstname'], 
                        lastname=request.POST['lastname'], 
                        email=request.POST['email'], 
                        passwordhash_decoded=mypasswordhash.decode()
                    )
                    request.session['successmessage'] = "Registration Successful!!  Welcome " + request.POST['firstname'] + "!"
                    return redirect("/success/")
                    # return render(request, "login_app/success.html")    
                else:
                    messages.add_message(request, messages.ERROR, "Unable to verify password and hash, bcrypt error")
    return redirect("/")



def logout(request):
    print("login")
    request.session['login_userid'] = 0
    return redirect("/")


def login(request):
    print("login")

    request.session['login_userid'] = 0
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
        if len(errors):
            print(errors)
            for key in errors:
                print(key,errors[key])
                messages.error(request, key + ":" + errors[key])
        else:
            if User.objects.filter(email=request.POST['loginemail']).exists():
                u1 = User.objects.get(email=request.POST['loginemail'])
                mypassword = request.POST['loginpassword'].encode()
                mypasswordhash = u1.passwordhash_decoded.encode()
                if bcrypt.checkpw(mypassword, mypasswordhash):
                    request.session['login_userid'] = u1.id
                    print("Password Verfied")
                    request.session['successmessage'] = "Login Successful!  Welcome " + u1.firstname + "!"
                    return redirect("/wall/")
                    # return render(request, "login_app/success.html")   
                else:
                    messages.add_message(request, messages.ERROR, "Unable to verify password and hash, invalid password")
            else:
                messages.add_message(request, messages.ERROR, "Email address not found in database")

    return redirect("/")


def success(request):
    print("success")
    if request.session['login_userid'] == 0:
        # registration successful render SUCCESS
        return render(request, "login_app/success.html")    
    # else:
    #     # login successful, redirect to wall
    #     return redirect("/wall/")

def wall(request):
    print("wall")
    myid = request.session['login_userid']
    return render(request, "login_app/wall.html", {'thisuser': User.objects.get(id=myid), 'allmessages': Message.objects.all().order_by('created_at').reverse()})    

def messagenew(request):
    print("messagenew")
    if request.method == "POST":
        myid = request.session['login_userid']
        if len(request.POST['message'])==0:
            messages.add_message(request, messages.ERROR, "Message Text must not be blank")
        else:
            m1 = Message.objects.create(
                message=request.POST['message'],                 
                user_id=myid,                 
            )
            messages.add_message(request, messages.SUCCESS, "Message submitted.")
            return redirect("/valid/")
    return redirect("/wall/")

def commentnew(request):
    print("commentnew")
    if request.method == "POST":
        if len(request.POST['comment'])==0:
            messages.add_message(request, messages.ERROR, "Comment Text must not be blank")
        else:
            if len(request.POST['message_id'])==0:
                messages.add_message(request, messages.ERROR, "Message ID is invalid")
            else:
                myid = request.session['login_userid']
                mymessageid = request.POST['message_id']
                c1 = Comment.objects.create(
                    comment=request.POST['comment'],
                    user_id=myid,
                    message_id=mymessageid
                )
                messages.add_message(request, messages.SUCCESS, "Comment submitted.")
                return redirect("/valid/")
    return redirect("/wall/")

def messagedestroy(request):
    print("messagedestroy")
    if request.method == "POST":
        if len(request.POST['message_id'])==0:
            messages.add_message(request, messages.ERROR, "Message ID not found")
        else:
            Message.objects.filter(id=request.POST['message_id']).delete()    
            messages.add_message(request, messages.SUCCESS, "Message deleted.")
            return redirect("/valid/")
    return redirect("/wall/")

def commentdestroy(request):
    print("commentdestroy")
    myid = request.session['login_userid']
    return redirect("/wall/")


def valid(request):
    print("valid")
    # new/delete successful, redirect to wall
    return redirect("/wall/")

