from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

# from time import gmtime, strftime
import datetime
import bcrypt
import random
import string
from decimal import *

# from django.utils import timezone
# from django.db import models
from .forms import *
from .models import User, Account, Delivery, Truck, Location, DataImport

# #################################################################
# 
# WE HAVE TO CREATE THIS FILE FROM SCRATCH EACH TIME
#
# #################################################################

def createdata(request):
    # if there are no accounts in the database we are going to create some so there is something to display

    # count()
    # Returns an integer representing the number of objects in the database matching the QuerySet. The count() method never raises exceptions.
    # Example:
    # # Returns the total number of entries in the database.
    # Entry.objects.count()

    iaccounts = Account.objects.count()
    if iaccounts == 0:

        t1 = Truck.objects.create(
            number = "1218",
            description = "2018 Freightliner 6300X",
            watercapacity = 3550,
            truckinspectiondate = datetime.datetime.now() - datetime.timedelta(weeks=random.uniform(5, 52)),
            tankinspectiondate = datetime.datetime.now() - datetime.timedelta(weeks=random.uniform(5, 52))
        )
        t2 = Truck.objects.create(
            number = "1472",
            description = "2017 Freightliner 6721R",
            watercapacity = 3600,
            truckinspectiondate = datetime.datetime.now() - datetime.timedelta(weeks=random.uniform(5, 52)),
            tankinspectiondate = datetime.datetime.now() - datetime.timedelta(weeks=random.uniform(5, 52))
        )
        t3 = Truck.objects.create(
            number = "5119",
            description = "2018 Freightliner 6377Z",
            watercapacity = 3480,
            truckinspectiondate = datetime.datetime.now() - datetime.timedelta(weeks=random.uniform(5, 52)),
            tankinspectiondate = datetime.datetime.now() - datetime.timedelta(weeks=random.uniform(5, 52))
        )
        t4 = Truck.objects.create(
            number = "6264",
            description = "2011 Western Star 101A",
            watercapacity = 2850,
            truckinspectiondate = datetime.datetime.now() - datetime.timedelta(weeks=random.uniform(35, 85)),
            tankinspectiondate = datetime.datetime.now() - datetime.timedelta(weeks=random.uniform(3, 85))
        )

        latstart = 47.6100000   # CODING DOJO LOCATION roughly
        longstart = -122.196400

        a1 = Account.objects.create(
            accountnumber = "00008", 
            name = "Andy Anderson", 
            address = "7742 52nd Ave S, Seattle, WA, 98118",
            latitude = 0,
            longitude = 0,
            latlong = "",
            phone = "",
            branch = 1,
            driver = str(int(random.uniform(1,10))),
            route = random.choice(string.ascii_uppercase),
            tanktype = 1,
            tanknumber = "A192834794",
            tanksize = 250
        )

        a2 = Account.objects.create(
            accountnumber = "00016", 
            name = "Barbara Billingsworth", 
            address = "10012 65th Ave S, Seattle, WA, 98178",
            latitude = random.uniform(latstart-0.5, latstart+0.5),
            longitude = random.uniform(longstart-0.5, longstart+0.5),
            latlong = "",
            phone = "",
            branch = 1,
            driver = str(int(random.uniform(1,10))),
            route = random.choice(string.ascii_uppercase),
            tanktype = 1,
            tanknumber = "A192275196",
            tanksize = 250
        )

        a3 = Account.objects.create(
            accountnumber = "00024", 
            name = "Craig & Cindy Chandler", 
            address = "3601 24th Ave W, APT 104, SEATTLE WA, 98199",
            latitude = random.uniform(latstart-0.5, latstart+0.5),
            longitude = random.uniform(longstart-0.5, longstart+0.5),
            latlong = "",
            phone = "",
            branch = 1,
            driver = str(int(random.uniform(1,10))),
            route = random.choice(string.ascii_uppercase),
            tanktype = 1,
            tanknumber = "A192305072",
            tanksize = 250
        )

        a4 = Account.objects.create(
            accountnumber = "00032", 
            name = "Doug and Doreen Dornan", 
            address = "4208 E Lynn St, Seattle, WA, 98112",
            latitude = random.uniform(latstart-0.5, latstart+0.5),
            longitude = random.uniform(longstart-0.5, longstart+0.5),
            latlong = "",
            phone = "",
            branch = 1,
            driver = str(int(random.uniform(1,10))),
            route = random.choice(string.ascii_uppercase),
            tanktype = 1,
            tanknumber = "A192720011",
            tanksize = 250
        )

        a5 = Account.objects.create(
            accountnumber = "00040", 
            name = "Elaine and Edward Ebenezer", 
            address = "828 NW 56th St, Seattle, WA, 98107",
            latitude = random.uniform(latstart-0.5, latstart+0.5),
            longitude = random.uniform(longstart-0.5, longstart+0.5),
            latlong = "",
            phone = "",
            branch = 1,
            driver = str(int(random.uniform(1,10))),
            route = random.choice(string.ascii_uppercase),
            tanktype = 1,
            tanknumber = "A192678345",
            tanksize = 250
        )

        a6 = Account.objects.create(
            accountnumber = "00048", 
            name = "Frank Fergusson", 
            address = "3419 30th Ave SW, Seattle, WA, 98126",
            latitude = random.uniform(latstart-0.5, latstart+0.5),
            longitude = random.uniform(longstart-0.5, longstart+0.5),
            latlong = "",
            phone = "",
            branch = 1,
            driver = str(int(random.uniform(1,10))),
            route = random.choice(string.ascii_uppercase),
            tanktype = 1,
            tanknumber = "A192205438",
            tanksize = 250
        )

        a7 = Account.objects.create(
            accountnumber = "00056", 
            name = "Greg Gunderson", 
            address = "2607 Western Ave, APT 456, Seattle, WA, 98121",
            latitude = random.uniform(latstart-0.5, latstart+0.5),
            longitude = random.uniform(longstart-0.5, longstart+0.5),
            latlong = "",
            phone = "",
            branch = 1,
            driver = str(int(random.uniform(1,10))),
            route = random.choice(string.ascii_uppercase),
            tanktype = 1,
            tanknumber = "A192073186",
            tanksize = 250
        )

        a8 = Account.objects.create(
            accountnumber = "00064", 
            name = "Herb and Henrietta Holt", 
            address = "2310 N 82nd St, Seattle, WA, 98103",
            latitude = random.uniform(latstart-0.5, latstart+0.5),
            longitude = random.uniform(longstart-0.5, longstart+0.5),
            latlong = "",
            phone = "",
            branch = 1,
            driver = str(int(random.uniform(1,10))),
            route = random.choice(string.ascii_uppercase),
            tanktype = 1,
            tanknumber = "A192271991",
            tanksize = 250
        )

        a9 = Account.objects.create(
            accountnumber = "00072", 
            name = "Irving and Ingrid Ingelbrook", 
            address = "3212 2nd Ave SE, Everett, WA, 98208",
            latitude = random.uniform(latstart-0.5, latstart+0.5),
            longitude = random.uniform(longstart-0.5, longstart+0.5),
            latlong = "",
            phone = "",
            branch = 1,
            driver = str(int(random.uniform(1,10))),
            route = random.choice(string.ascii_uppercase),
            tanktype = 1,
            tanknumber = "A192430977",
            tanksize = 250
        )

        a10 = Account.objects.create(
            accountnumber = "00081", 
            name = "John and Jacqueline Jergens", 
            address = "3504 172nd St SW, Lynnwood, WA, 98037",
            latitude = random.uniform(latstart-0.5, latstart+0.5),
            longitude = random.uniform(longstart-0.5, longstart+0.5),
            latlong = "",
            phone = "",
            branch = 1,
            driver = str(int(random.uniform(1,10))),
            route = random.choice(string.ascii_uppercase),
            tanktype = 1,
            tanknumber = "A192003775",
            tanksize = 250
        )

        a11 = Account.objects.create(
            accountnumber = "00089", 
            name = "Kris Kringle", 
            address = "305 N 4th St, Tacoma, WA, 98403",
            latitude = random.uniform(latstart-0.5, latstart+0.5),
            longitude = random.uniform(longstart-0.5, longstart+0.5),
            latlong = "",
            phone = "",
            branch = 1,
            driver = str(int(random.uniform(1,10))),
            route = random.choice(string.ascii_uppercase),
            tanktype = 1,
            tanknumber = "A192000001",
            tanksize = 250
        )



        # 4 trucks created
        # 11 accounts created
        for i in range(1,12):
            # addrandomdelivery(request, random.uniform(1, int(str(Account.objects.latest('id').id))), random.uniform(1, int(str(Truck.objects.latest('id').id))))
            for j in range(1,5):
                addrandomdelivery(request, i, random.uniform(1, int(str(Truck.objects.latest('id').id))))
                addrandomdelivery(request, random.uniform(1, int(str(Account.objects.latest('id').id))), j)

        for i in range(1,21):
            addrandomdelivery(request, random.uniform(1, int(str(Account.objects.latest('id').id))), random.uniform(1, int(str(Truck.objects.latest('id').id))))

    return


# /Users/bart/anaconda3/envs/pipenv-py36-aws/lib/python3.6/site-packages/django/db/models/fields/__init__.py:1423: 
# RuntimeWarning: DateTimeField Delivery.finishdate received a naive datetime (2018-06-27 18:26:16.539255) 
# while time zone support is active. RuntimeWarning)
# [27/Jun/2018 21:10:16] "GET /main/ HTTP/1.1" 200 1120



def initsession(request):
    if 'successmessage' not in request.session:
        request.session['successmessage'] = ""
        request.session['login_userid'] = 0
    return

def index(request):
    initsession(request)
    print("index")
    return render(request, "importer/index.html", {'allusers': User.objects.all(), 'loginform': LoginForm(), 'registerform': RegisterForm()})
    # return render(request, "importer/index.html")    

def register(request):
    print("register")
    if request.method == "POST":
        errors = User.objects.create_validator(request.POST)
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
                            name=request.POST['name'], 
                            company=request.POST['company'], 
                            email=request.POST['email'], 
                            passwordhash_decoded=mypasswordhash.decode()
                        )
                        request.session['successmessage'] = "Registration Successful, Welcome!!  Please use " + request.POST['email'] + " to login."
                    else:
                        messages.add_message(request, messages.ERROR, "Unable to verify password")
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
                    return redirect("/main/")
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


def mainindex(request):
    print("mainindex")
    myid = request.session['login_userid']
    createdata(request)
    return render(request, "importer/main.html", {'thisuser': User.objects.get(id=myid), 'alldeliveries': Delivery.objects.all().order_by('created_at'), 'allaccounts': Account.objects.all().order_by('accountnumber') } )    


def accounts(request):
    print("accounts")
    myid = request.session['login_userid']
    return render(request, "importer/accounts.html", {'thisuser': User.objects.get(id=myid), 'allaccounts': Account.objects.all().order_by('accountnumber') })

def deliveries(request):
    print("deliveries")
    myid = request.session['login_userid']
    return render(request, "importer/deliveries.html", {'thisuser': User.objects.get(id=myid), 'alldeliveries': Delivery.objects.all().order_by('created_at') })

def deliveriesmap(request):
    print("deliveriesmap")
    myid = request.session['login_userid']
    alldeliveries = Delivery.objects.all().order_by('created_at')
    alllocations = []
    for deliv in alldeliveries:
        mylist = []
        print(deliv.account.name, deliv.account.address, deliv.latitude, deliv.longitude)
        mylist.append(deliv.account.name + "<br> " + deliv.account.address + "<br> <a href='/account/" + str(deliv.account.id) + "/view/'>Account</a> <a href='/truck/" + str(deliv.truck.id) + "/view/'>Truck</a> <a href='/delivery/" + str(deliv.id) + "/view/'>Delivery</a>")
        mylist.append(str(deliv.latitude))
        mylist.append(str(deliv.longitude))
        alllocations.append(mylist)
    return render(request, "importer/deliveriesmap.html", {'thisuser': User.objects.get(id=myid), 'alldeliveries': alldeliveries, 'allaccounts': Account.objects.all().order_by('accountnumber'), 'alllocations': alllocations } )    

def truckdeliveriesmap(request, truck_id):
    print("truckdeliveriesmap Truck.id = " + str(truck_id))
    myid = request.session['login_userid']
    t1 = Truck.objects.get(id=truck_id)
    alldeliveries = Delivery.objects.filter(truck=t1)
    alllocations = []
    for deliv in alldeliveries:
        mylist = []
        print(deliv.account.name, deliv.account.address, deliv.latitude, deliv.longitude)
        mylist.append(deliv.account.name + "<br> " + deliv.account.address + "<br> <a href='/account/" + str(deliv.account.id) + "/view/'>Account</a> <a href='/truck/" + str(deliv.truck.id) + "/view/'>Truck</a> <a href='/delivery/" + str(deliv.id) + "/view/'>Delivery</a>")
        mylist.append(str(deliv.latitude))
        mylist.append(str(deliv.longitude))
        alllocations.append(mylist)
    return render(request, "importer/deliveriesmap.html", {'thisuser': User.objects.get(id=myid), 'alldeliveries': alldeliveries, 'allaccounts': Account.objects.all().order_by('accountnumber'), 'alllocations': alllocations } )    

def accountdeliveriesmap(request, account_id):
    print("accountdeliveriesmap Account.id = " + str(account_id))
    myid = request.session['login_userid']
    a1 = Account.objects.get(id=account_id)
    alldeliveries = Delivery.objects.filter(account=a1)
    alllocations = []
    for deliv in alldeliveries:
        mylist = []
        print(deliv.account.name, deliv.account.address, deliv.latitude, deliv.longitude)
        mylist.append(deliv.account.name + "<br> " + deliv.account.address + "<br> <a href='/account/" + str(deliv.account.id) + "/view/'>Account</a> <a href='/truck/" + str(deliv.truck.id) + "/view/'>Truck</a> <a href='/delivery/" + str(deliv.id) + "/view/'>Delivery</a>")
        mylist.append(str(deliv.latitude))
        mylist.append(str(deliv.longitude))
        alllocations.append(mylist)
    return render(request, "importer/deliveriesmap.html", {'thisuser': User.objects.get(id=myid), 'alldeliveries': alldeliveries, 'allaccounts': Account.objects.all().order_by('accountnumber'), 'alllocations': alllocations } )    

def deliverymap(request, delivery_id):
    print("deliverymap Delivery.id = " + str(delivery_id))
    myid = request.session['login_userid']
    alldeliveries = Delivery.objects.filter(id=delivery_id)
    alllocations = []
    for deliv in alldeliveries:
        mylist = []
        print(deliv.account.name, deliv.account.address, deliv.latitude, deliv.longitude)
        mylist.append(deliv.account.name + "<br> " + deliv.account.address + "<br> <a href='/account/" + str(deliv.account.id) + "/view/'>Account</a> <a href='/truck/" + str(deliv.truck.id) + "/view/'>Truck</a> <a href='/delivery/" + str(deliv.id) + "/view/'>Delivery</a>")
        mylist.append(str(deliv.latitude))
        mylist.append(str(deliv.longitude))
        alllocations.append(mylist)
    return render(request, "importer/deliveriesmap.html", {'thisuser': User.objects.get(id=myid), 'alldeliveries': alldeliveries, 'allaccounts': Account.objects.all().order_by('accountnumber'), 'alllocations': alllocations } )    


def accountmap(request, account_id):
    print("accountmap Account.id = " + str(account_id))
    myid = request.session['login_userid']
    alldeliveries = Delivery.objects.all().order_by('created_at')
    a1 = Account.objects.get(id=account_id)
    return render(request, "importer/geocodemap.html", {'thisuser': User.objects.get(id=myid), 'thisaccount': a1, 'alldeliveries': alldeliveries, 'allaccounts': Account.objects.all().order_by('accountnumber') } )    


def trucks(request):
    print("trucks")
    myid = request.session['login_userid']
    return render(request, "importer/trucks.html", {'thisuser': User.objects.get(id=myid), 'alltrucks': Truck.objects.all().order_by('number') })


# url(r'^myaccount/(?P<user_id>\d+)/edit$', views.edituser),  
#     # GET render edit template for current user
def edituser(request, user_id):
    print("edituser User.id = " + str(user_id))
    myid = request.session['login_userid']
    if (myid != user_id):
        print(myid, user_id, "How the hell did it get here")

        u1 = User.objects.get(id=myid)
        initial={'name': u1.name, 'company': u1.company, 'email': u1.email }
        r = RegisterUpdateForm(initial)
    return render(request, "importer/myaccount.html", {'thisuser': u1, 'registerupdateform': r })

# url(r'^myaccount/update$', views.updateuser),  
#     # POST update user data from form
#     # process request, 
#     # redirect to myaccount if valid or 
#     # redirect to myaccount if error
def updateuser(request):
    print("updateuser")
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

                    u1.name=request.POST['name']
                    u1.company=request.POST['company']
                    u1.email=request.POST['email']
                    u1.save()

                    messages.add_message(request, messages.SUCCESS, "Account updated.")

                else:
                    messages.add_message(request, messages.ERROR, "Requested EMail reserved, try another")
            else:
                u1 = User.objects.get(id=myid)
                print(u1, u1.id)

                u1.name=request.POST['name']
                u1.company=request.POST['company']
                u1.email=request.POST['email']
                u1.save()

                messages.add_message(request, messages.SUCCESS, "Account updated.")

    return redirect("/myaccount/" + str(myid)  + "/edit/")



# url(r'^import/$', views.importselect),  
#     # GET render import data page
def importselect(request):
    print("importselect")
    myid = request.session['login_userid']
    u1 = User.objects.get(id=myid)
    return render(request, "importer/selectimport.html", {'thisuser': User.objects.get(id=myid), 'myimports': DataImport.objects.filter(user=u1)} )


# url(r'^import/verify/$', views.importverify),  
#     # POST create new import from POST data from form
#     # process request, 
#     # redirect to main if valid or 
#     # redirect to import if error
def importverify(request):
    print("importverify")
    myid = request.session['login_userid']
    thisimportid = 1
    u1 = User.objects.get(id=myid)
    i1 = DataImport.objects.get(id=thisimportid)
    return render(request, "importer/verifyimport.html", {'thisuser': User.objects.get(id=myid), 'thisimport':i1,'myimports': DataImport.objects.filter(user=u1)} )





def viewaccount(request, account_id):
    print("viewaccount Account.id = " + str(account_id))
    myid = request.session['login_userid']
    u1 = User.objects.get(id=myid)
    a1 = Account.objects.get(id=account_id)
    af = AccountForm(None, instance=a1)
    d1 = Delivery.objects.filter(account=a1.id).order_by('finishdate')
    return render(request, "importer/account.html", {'thisuser': u1, 'thisaccount':a1, 'accountform': af , 'thisdeliveries': d1 })





def viewtruck(request, truck_id):
    print("viewtruck Truck.id = " + str(truck_id))
    myid = request.session['login_userid']
    u1 = User.objects.get(id=myid)
    t1 = Truck.objects.get(id=truck_id)
    tf = TruckForm(None, instance=t1)
    d1 = Delivery.objects.filter(truck=truck_id).order_by('finishdate')
    return render(request, "importer/truck.html", {'thisuser': u1, 'thistruck':t1, 'truckform': tf, 'thisdeliveries':d1 })

def viewdelivery(request, delivery_id):
    print("viewdelivery Delivery.id = " + str(delivery_id))
    myid = request.session['login_userid']
    u1 = User.objects.get(id=myid)
    d1 = Delivery.objects.get(id=delivery_id)
    df = DeliveryForm(None, instance=d1)
    return render(request, "importer/delivery.html", {'thisuser': u1, 'thisdelivery':d1, 'deliveryform': df })


def importupload(request):
    if request.method == "POST":
        handle_uploaded_file(request.FILES['file'], str(request.FILES['file']))
        return HttpResponse("<h1> HOLY $%^T YOU JUST UPLOADED A FILE TO YOUR OWN PC</h1><br><p><a href='/import/'>GO BACK</a></p>")

    return HttpResponse("Failed")
        
def handle_uploaded_file(file, filename):
    # if not os.path.exists('upload/'):
    #     os.mkdir('upload/')
    with open('upload/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

def randdelivery(request):
    addrandomdelivery(request, random.uniform(1, int(str(Account.objects.latest('id').id))), random.uniform(1, int(str(Truck.objects.latest('id').id))))
    return redirect("/deliveries/")

def randaccountdelivery(request, account_id):
    # t1 = Truck.objects.latest('id')
    addrandomdelivery(request, account_id, random.uniform(1, int(str(Truck.objects.latest('id').id))))
    return redirect("/account/" + str(account_id) + "/view/#deliveries")

def randtruckdelivery(request, truck_id):
    # a1 = Account.objects.latest('id')
    addrandomdelivery(request, random.uniform(1, int(str(Account.objects.latest('id').id))), truck_id)
    return redirect("/truck/" + str(truck_id) + "/view/#deliveries")

def addrandomdelivery(request, account_id, truck_id):

    ay = Account.objects.get(id=account_id)
    ty = Truck.objects.get(id=truck_id)

    tots = random.uniform(100000,200000)
    vol = random.uniform(25.0, 205.0)
    spct = random.uniform(10.0, 50.9)
    price = random.uniform(3.799, 4.799)
    amt = vol*price
    ticket = int(random.uniform(100, 400))
    sale = int(random.uniform(600, 900))

    lat = 0
    long = 0
    if ay.latitude==0.0:
        lat = random.uniform(47.63555, 47.65555)
        long = random.uniform(-122.35, -122.31)
    else:
        lat = ay.latitude  + Decimal(str(random.uniform(-0.01, 0.01)))
        long = ay.longitude  + Decimal(str(random.uniform(-0.03, 0.03)))

    totf = vol + tots

    dy = Delivery.objects.create(

        account = ay,
        routenumber = ay.route,

        truck = ty,
        drivernumber = ay.driver,
        trucknumber = ty.number,

        volume = vol,
        percent_full_start = spct,
        percent_full_end = spct + (vol / ay.tanksize) * 100,
        totalcost = amt,
        productcode = "01",
        productdesc = "Residential Propane On-Route",
        ticketnumber = ticket,
        salenumber = sale,
        registernumber = 1,
        registerserialnumber = "010921",
        registertype = "ECOUNT",
        tempcompensated = "ON",

        latitude = lat,
        longitude = long,
        latlong = "",

        startdate = datetime.datetime.now() - datetime.timedelta(minutes=2, seconds=59),
        finishdate = datetime.datetime.now(),
        starttotalizer = tots,
        finishtotalizer = totf
    )
    print("Delivery created for account id " + str(account_id) + ", truck_id " + str(truck_id))

    return