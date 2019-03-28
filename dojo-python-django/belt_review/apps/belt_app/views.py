from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

# from time import gmtime, strftime
# import datetime
import bcrypt

# from django.utils import timezone
# from django.db import models
from .models import User
from .models import Review
from .models import Book
from .models import Author

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
    return render(request, "belt_app/index.html", {'allusers': User.objects.all()})    

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
            else:
                if User.objects.filter(email=request.POST['email']).exists():
                    messages.add_message(request, messages.ERROR, "Email address already exists in database")
                else:
                    mypassword = request.POST['password1'].encode()
                    mypasswordhash = bcrypt.hashpw(mypassword, bcrypt.gensalt())
                    if bcrypt.checkpw(mypassword, mypasswordhash):
                        print("New Password Verfied, storing ..")
                        u1 = User.objects.create(
                            username=request.POST['username'], 
                            useralias=request.POST['useralias'], 
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
                messages.error(request, key + ":" + errors[key])
        else:
            if User.objects.filter(email=request.POST['loginemail']).exists():
                u1 = User.objects.get(email=request.POST['loginemail'])
                mypassword = request.POST['loginpassword'].encode()
                mypasswordhash = u1.passwordhash_decoded.encode()
                if bcrypt.checkpw(mypassword, mypasswordhash):
                    request.session['login_userid'] = u1.id
                    print("Password Verfied")
                    request.session['successmessage'] = ""
                    return redirect("/books/")
                else:
                    messages.add_message(request, messages.ERROR, "Unable to verify password and hash, invalid password")
            else:
                messages.add_message(request, messages.ERROR, "Email address not found in database")

    return redirect("/")

def logout(request):
    print("logout")
    messages.add_message(request, messages.ERROR, "Logout Successful")
    request.session['login_userid'] = 0
    return redirect("/")



def booksindex(request):
    print("booksindex")
    myid = request.session['login_userid']
    return render(request, "belt_app/books.html", {'thisuser': User.objects.get(id=myid), 'allreviews': Review.objects.all().order_by('created_at'), 'allbooks': Book.objects.all()})    

def booksshowbook(request, book_id):
    print("booksshowbook Book.id = " + str(book_id))
    myid = request.session['login_userid']
    return render(request, "belt_app/show.html", {'thisbook':Book.objects.get(id=book_id), 'thisuser': User.objects.get(id=myid), 'allreviews': Review.objects.filter(book_id=book_id).order_by('created_at')})

def booksnew(request):
    print("booksnew")
    myid = request.session['login_userid']
    return render(request, "belt_app/new.html", {'thisuser': User.objects.get(id=myid), 'allreviews': Review.objects.all().order_by('created_at')})


def bookscreate(request):
    print("bookscreate")
    if request.method == "POST":
        myid = request.session['login_userid']
        print(request.POST)

        errors = Book.objects.review_validator(request.POST)
        if len(errors):
            print(errors)
            for key in errors:
                print(key,errors[key])
                messages.error(request, key + ":" + errors[key])
        else:

            # Add:
            # 1. author
            # 2. book
            # 3. review

            u1 = User.objects.get(id=myid)
            print(u1, u1.id)

            if "author_id" not in request.POST:
                a1 = Author.objects.create(
                    authorname = request.POST['author_name']
                )
            else:
                a1 = Author.objects.get(
                    id = request.POST['author_id']
                )
            print(a1)

            if "book_id" not in request.POST:
                b1 = Book.objects.create(
                    author = a1, 
                    title  = request.POST['book_title']
                )
            else:
                b1 = Book.objects.get(
                    id  = request.POST['book_id']
                )
            print(b1)

            r1 = Review.objects.create(
                user   = u1,
                book   = b1, 
                review = request.POST['review_text'], 
                rating = request.POST['book_rating']
            )
            print(r1)

            return redirect("/books/" + str(b1.id) + "/showbook/")

    return redirect("/books/")



def booksshowuser(request, user_id):
    print("booksshowuser User.id = " + str(user_id))
    thisuser = User.objects.get(id=user_id)
    return render(request, "belt_app/showuser.html", {'thisuser': User.objects.get(id=user_id), 'myreviews': Review.objects.filter(user=thisuser).order_by('created_at'), 'mybooks': Book.objects.filter(user=thisuser)})    


def booksdestroyreview(request, book_id, review_id):
    print("booksdestroyreview")
    myid = request.session['login_userid']

    print("=============================   NEED TO MAKE SURE WE SUBMITTED THIS REVIEW   ================================")
    Review.objects.filter(id=request.POST['review_id']).delete()    
    messages.add_message(request, messages.SUCCESS, "Review deleted.")
    return redirect("/books/" + book_id + "/showbook/")

