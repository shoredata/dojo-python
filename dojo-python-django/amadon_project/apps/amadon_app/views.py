from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
# from django.utils import timezone
# from django.db import models

from decimal import Decimal
# from time import gmtime, strftime
# import datetime
from .models import Product

# #################################################################
# 
# WE HAVE TO CREATE THIS FILE FROM SCRATCH EACH TIME!!!!!!!!!!!!!!!
#
# #################################################################

# urlpatterns = [
#     url(r'^$', views.index),    
#         # GET list all products, render template INDEX
#     url(r'^buy/$', views.buy),  
#         # POST creates purchase data in db, redirect to checkout
#     url(r'^checkout/$', views.checkout),  
#         # GET renders checkout (has href to index)
# ]

def initsession(request):
    if 'invoicecharged' not in request.session:
        request.session['invoicecharged'] = "0"
        request.session['totalitems'] = "0"
        request.session['totalcharged'] = "0"
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



def index(request):
    # print("index")
    # print(type(Product.objects.all()))
    # print(Product.objects.all().count())
    initsession(request)
    if (Product.objects.all().count()==0):
        # insert some products
        print("Creating some products")
        Product.objects.create(name='Dojo T-Shirt', price=19.99)
        Product.objects.create(name='Dojo Sweater', price=29.99)
        Product.objects.create(name='Dojo Cup', price=19.99)
        Product.objects.create(name='Algorithm Book', price=49.99)
    return render(request, "amadon_app/index.html", {'allproducts': Product.objects.all()})    

def buy(request):
    # print("buy")
    if request.method == "POST":
        # print(request.POST)
        prod = Product.objects.get(id=request.POST['product_id'])
        myqty = int(request.POST['order_quantity'])
        prod.ordered_quantity += myqty
        prod.save()
        myprice = prod.price
        myamount = myqty * myprice

        # printsession(request, "pre-buy")

        itotalitems = int(request.session['totalitems'])
        itotalitems += myqty

        dtotalcharged = Decimal(request.session['totalcharged'])
        dtotalcharged += myamount

        request.session['invoicecharged'] = str(myamount)
        request.session['totalitems'] = str(itotalitems)
        request.session['totalcharged'] = str(dtotalcharged)

        # printsession(request, "post-buy")

        return redirect("/checkout/")
    else:
        return redirect("/")        

def checkout(request):
    # print("checkout")
    return render(request, "amadon_app/checkout.html")    
