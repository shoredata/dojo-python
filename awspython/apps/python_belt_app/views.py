from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

# from time import gmtime, strftime
# import datetime
import bcrypt

# from django.utils import timezone
# from django.db import models
from .models import User, Quote, Like

# #################################################################
# 
# WE HAVE TO CREATE THIS FILE FROM SCRATCH EACH TIME!!!!!!!!!!!!!!!
#
# #################################################################

def initsession(request):
    if 'successmessage' not in request.session:
        request.session['successmessage'] = ""
        request.session['login_userid'] = 0
    return

def index(request):
    initsession(request)
    print("index")
    # return render(request, "python_belt_app/index.html", {'allusers': User.objects.all()})    
    return render(request, "python_belt_app/index.html")    

def register(request):
    print("register")
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors):
            print(errors)
            for key in errors:
                print(key,errors[key])
                # messages.error(request, key + ":" + errors[key])
                messages.error(request, errors[key])
        else:
            if request.POST['password1'] != request.POST['password2']:
                messages.add_message(request, messages.ERROR, "Passwords do not match")
            else:
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
                        request.session['successmessage'] = "Registration Successful, Welcome!!  Please use " + request.POST['email'] + " to login."
                    else:
                        messages.add_message(request, messages.ERROR, "Unable to verify password and hash, bcrypt error")
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
                # messages.error(request, key + ":" + errors[key])
                messages.error(request, errors[key])
        else:
            if User.objects.filter(email=request.POST['loginemail']).exists():
                u1 = User.objects.get(email=request.POST['loginemail'])
                mypassword = request.POST['loginpassword'].encode()
                mypasswordhash = u1.passwordhash_decoded.encode()
                if bcrypt.checkpw(mypassword, mypasswordhash):
                    request.session['login_userid'] = u1.id
                    print("Password Verfied")
                    request.session['successmessage'] = ""
                    return redirect("/quotes/")
                else:
                    messages.add_message(request, messages.ERROR, "Unable to verify password and hash, invalid password")
            else:
                messages.add_message(request, messages.ERROR, "Email address not found in database")

    return redirect("/")

def logout(request):
    print("logout")
    messages.add_message(request, messages.SUCCESS, "Logout Successful")
    request.session['login_userid'] = 0
    return redirect("/")


def quotesindex(request):
    print("quotesindex")
    myid = request.session['login_userid']
    return render(request, "python_belt_app/quotes.html", {'thisuser': User.objects.get(id=myid), 'allquotes': Quote.objects.all().order_by('created_at')})    


def quotesbyuser(request, user_id):
    print("quotesbyuser User.id = " + str(user_id))
    myid = request.session['login_userid']
    # return render(request, "python_belt_app/user.html", {'thisuser': User.objects.get(id=myid), 'allquotes': Quote.objects.all().order_by('created_at')})
    ux = User.objects.get(id=user_id)
    return render(request, "python_belt_app/user.html", {'showuser': User.objects.get(id=ux.id) , 'thisuser': User.objects.get(id=myid), 'allquotes': Quote.objects.filter(user=ux).order_by('created_at')})


def quotesedituser(request, user_id):
    print("quotesedituser User.id = " + str(user_id))
    myid = request.session['login_userid']
    if (myid != user_id):
        print(myid, user_id, "How the hell did it get here")
    return render(request, "python_belt_app/myaccount.html", {'thisuser': User.objects.get(id=myid)})



def quotesupdateuser(request):
    print("quotesupdateuser")
    myid = request.session['login_userid']

    print(request.POST)
    if request.method == "POST":
        errors = User.objects.edit_validator(request.POST)
        if len(errors):
            print(errors)
            for key in errors:
                print(key,errors[key])
                # messages.error(request, key + ":" + errors[key])
                messages.error(request, errors[key])
        else:
            if User.objects.filter(email=request.POST['email']).exists():
                u1 = User.objects.get(email=request.POST['email'])
                if u1.id == myid:

                    u1.firstname=request.POST['firstname']
                    u1.lastname=request.POST['lastname']
                    u1.email=request.POST['email']
                    u1.save()

                    messages.add_message(request, messages.SUCCESS, "Account updated.")

                else:
                    messages.add_message(request, messages.ERROR, "Requested EMail reserved, try another")
            else:
                u1 = User.objects.get(id=myid)
                print(u1, u1.id)

                u1.firstname=request.POST['firstname']
                u1.lastname=request.POST['lastname']
                u1.email=request.POST['email']
                u1.save()

                messages.add_message(request, messages.SUCCESS, "Account updated.")

    return redirect("/quotes/myaccount/" + str(myid) +"/")



def quotescreatequote(request):
    print("quotescreatequote")
    myid = request.session['login_userid']
    print(request.POST)
    if request.method == "POST":
        errors = Quote.objects.create_validator(request.POST)
        if len(errors):
            print(errors)
            for key in errors:
                print(key,errors[key])
                # messages.error(request, key + ":" + errors[key])
                messages.error(request, errors[key])
        else:
            u1 = User.objects.get(id=myid)
            print(u1, u1.id)

            if Quote.objects.filter(
                text=request.POST['quotetext'], 
                author=request.POST['author']).exists():
                messages.add_message(request, messages.ERROR, "Quote+Author Already Exists!")
            else:
                q1 = Quote.objects.create(
                    user   = u1,
                    text=request.POST['quotetext'], 
                    author=request.POST['author']
                )
                print(q1)

    return redirect("/quotes/")



def quotesdeletequote(request, quote_id):
    print("quotesedituser Quote.id = " + str(quote_id))
    myid = request.session['login_userid']

    print("=============================   NEED TO MAKE SURE WE SUBMITTED THIS REVIEW   ================================")
    Quote.objects.filter(id=quote_id).delete()    
    messages.add_message(request, messages.SUCCESS, "Quote deleted.")
    return redirect("/quotes/")



def quoteslike(request):
    print("quoteslike")
    myid = request.session['login_userid']

    print(request.POST)
    if request.method == "POST":

        u1 = User.objects.get(id=myid)
        print(u1, u1.id)

        myquoteid = request.POST['quote_id']

        q1 = Quote.objects.get(id=myquoteid)
        print(q1, q1.id)

        if Like.objects.filter(
            user=u1, 
            quote=q1).exists():
            messages.add_message(request, messages.ERROR, "You already like this quote!!")
        else:
            l1 = Like.objects.create(
                user   = u1,
                quote = q1
            )
            print(l1)
            messages.add_message(request, messages.SUCCESS, "YAY!!! You liked that quote! Look for more!!!")

    return redirect("/quotes/")
