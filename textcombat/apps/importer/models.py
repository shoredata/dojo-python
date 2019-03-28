from __future__ import unicode_literals
from django.db import models

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class TruckManager(models.Manager):
    def create_validator(self, postData):
        errors = {}
        if len(postData['number']) < 1:
            errors["number1"] = "Truck Number should not be blank"
        if len(postData['number']) > 255:
            errors["number255"] = "Truck Number should be less than 256 characters"
        return errors

class AccountManager(models.Manager):
    def create_validator(self, postData):
        errors = {}
        if len(postData['name']) < 1:
            errors["name1"] = "Name should not be blank"
        if len(postData['name']) > 255:
            errors["name255"] = "Name should be less than 256 characters"
        if len(postData['account']) < 1:
            errors["account1"] = "Account # should not be blank"
        if len(postData['account']) > 255:
            errors["account255"] = "Account # should be less than 256 characters"
        print("Make sure account # does not already exist")
        return errors

class DeliveryManager(models.Manager):
    def create_validator(self, postData):
        errors = {}
        if len(postData['truck']) < 1:
            errors["truck"] = "Truck should not be blank"
        if len(postData['account']) < 1:
            errors["account"] = "Account should not be blank"
        print("Make sure sale-#/date-time/pc/cost does not already exist")
        return errors

class LocationManager(models.Manager):
    def create_validator(self, postData):
        errors = {}
        if len(postData['truck']) < 1:
            errors["truck"] = "Truck should not be blank"
        print("Make sure lat/long/driver exists on record")
        return errors

class UserManager(models.Manager):
    def login_validator(self, postData):
        errors = {}
        if len(postData['loginemail']) <= 5:
            errors["email"] = "EMail/Password not valid"
        if len(postData['loginpassword']) <= 7:
            errors["password"] = "EMail/Password not valid"
        return errors


    def edit_validator(self, postData):
        errors = {}
        if len(postData['name']) < 1:
            errors["name1"] = "Name should not be blank"
        if len(postData['name']) > 255:
            errors["name255"] = "Name should be less than 256 characters"

        if len(postData['company']) < 1:
            errors["company1"] = "Company should not be blank"
        if len(postData['company']) > 255:
            errors["company255"] = "Company should be less than 256 characters"

        if len(postData['email']) < 1:
            errors["email1"] = "EMail should not be blank"
        if not EMAIL_REGEX.match(postData['email']):   
            errors["emailchars"] = "EMail format invalid (alpha.numeric@domain.tld)"
        if len(postData['email']) > 255:
            errors["email255"] = "EMail should be less than 256 characters"

        return errors


    def create_validator(self, postData):
        errors = self.edit_validator(postData)

        if len(postData['password1']) <= 7:
            errors["password7"] = "Password should be more than 7 characters"
        if len(postData['password1']) > 255:
            errors["password256"] = "Password should be less than 256 characters"

        x = False
        while not x:  
            if not re.search("[a-z]",postData['password1']):
                errors["passwordlower"] = "Password requires a lowercase letter"
                break
            elif not re.search("[0-9]",postData['password1']):
                errors["passwordnum"] = "Password requires a numeric character"
                break
            elif not re.search("[A-Z]",postData['password1']):
                errors["passwordupper"] = "Password requires an uppercase letter"
                break
            elif re.search("\s",postData['password1']):
                errors["passwordchars"] = "Password contains invalid character(s)"
                break
            else:
                x=True
                break
        return errors




class User(models.Model):
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    passwordhash_decoded = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

    def __repr__(self):
        return "<User object: {} {} {}>".format(self.name, self.company, self.email)
    def __str__(self):
        return "<User object:: {} {} {}>".format(self.name, self.company, self.email)


class Truck(models.Model):
    number = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    truckinspectiondate = models.DateTimeField(auto_now=False)
    tankinspectiondate = models.DateTimeField(auto_now=False)
    watercapacity = models.IntegerField()

    # TicketPrinterType
    # RegisterType
    # GPSType

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = TruckManager()

    def __repr__(self):
        return "<Truck object: {} {}>".format(self.number, self.description)
    def __str__(self):
        return "<Truck object:: {} {}>".format(self.number, self.description)


# Latitudes range from -90 to +90 (degrees), so DECIMAL(10, 8) is ok for that, 
# but longitudes range from -180 to +180 (degrees) so you need DECIMAL(11, 8). 
# The first number is the total number of digits stored, and the second is the 
# number after the decimal point.

class Account(models.Model):
    accountnumber = models.CharField(max_length=16)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)
    latlong = models.CharField(max_length=48)
    phone = models.CharField(max_length=48)
    branch = models.CharField(max_length=32)
    driver = models.CharField(max_length=8)
    route = models.CharField(max_length=8)
    tanktype = models.CharField(max_length=8)
    tanknumber = models.CharField(max_length=32)
    tanksize = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = AccountManager()

    def __repr__(self):
        return "<Account object: {} {} {}>".format(self.accountnumber,self.name,self.address)
    def __str__(self):
        return "<Account object:: {} {} {}>".format(self.accountnumber,self.name,self.address)


class Delivery(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name = "deliveries")
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE, related_name = "deliveries")

    drivernumber = models.CharField(max_length=8)
    routenumber = models.CharField(max_length=8)
    trucknumber = models.CharField(max_length=8)

    startdate = models.DateTimeField(auto_now=False)
    finishdate = models.DateTimeField(auto_now=False)
    starttotalizer = models.DecimalField(max_digits=12, decimal_places=2)
    finishtotalizer = models.DecimalField(max_digits=12, decimal_places=2)

    volume = models.DecimalField(max_digits=12, decimal_places=2)
    percent_full_start = models.IntegerField()
    percent_full_end = models.IntegerField()
    totalcost = models.DecimalField(max_digits=12, decimal_places=2)
    productcode = models.CharField(max_length=8)
    productdesc = models.CharField(max_length=128)
    ticketnumber = models.CharField(max_length=16)
    salenumber = models.CharField(max_length=16)
    registernumber = models.IntegerField()
    registerserialnumber = models.CharField(max_length=16)
    registertype = models.CharField(max_length=16)
    tempcompensated = models.CharField(max_length=8)
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)
    latlong = models.CharField(max_length=48)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = DeliveryManager()

    def __repr__(self):
        return "<Delivery object: {} {} {} {} {}>".format(self.account, self.truck, self.startdate, self.salenumber, self.volume)
    def __str__(self):
        return "<Delivery object:: {} {} {} {} {}>".format(self.account, self.truck, self.startdate, self.salenumber, self.volume)


class Location(models.Model):
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE, related_name = "locations")
    origin_acct = models.ForeignKey(Account, on_delete=models.CASCADE, related_name = "locations_next")
    destination_acct = models.ForeignKey(Account, on_delete=models.CASCADE, related_name = "locations_previous")

    drivernumber = models.CharField(max_length=8)
    routenumber = models.CharField(max_length=8)
    trucknumber = models.CharField(max_length=8)

    localdate = models.DateTimeField(auto_now=False)

    notes = models.CharField(max_length=255)

    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)
    latlong = models.CharField(max_length=48)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = LocationManager()

    def __repr__(self):
        return "<Location object: {} {} {} {}>".format(self.truck, self.drivernumber, self.latitude, self.longitude)
    def __str__(self):
        return "<Location object:: {} {} {} {}>".format(self.truck, self.drivernumber, self.latitude, self.longitude)


class DataImport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "data_imports")

    filenameonly = models.CharField(max_length=255)
    filefullpath = models.CharField(max_length=255)
    filefolderonly = models.CharField(max_length=255)

    summary_file = models.CharField(max_length=255)

    count_accounts = models.IntegerField()
    count_deliveries = models.IntegerField()
    count_locations = models.IntegerField()
    count_loads = models.IntegerField()
    count_blankaccounts = models.IntegerField()
    count_blankloads = models.IntegerField()
    file_version = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # objects = DataImportManager()

    def __repr__(self):
        return "<DataImport object: {} {} {} {} {} {}>".format(self.filenameonly, self.user, self.created_at, self.count_accounts, self.count_deliveries, self.count_locations)
    def __str__(self):
        return "<DataImport object:: {} {} {} {} {} {}>".format(self.filenameonly, self.user, self.created_at, self.count_accounts, self.count_deliveries, self.count_locations)

class Option(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="options")

    CompanyCode = models.CharField(max_length=10)

    SDFileAdditionalDataFields = models.CharField(max_length=1)
    SDAccountNumberLength = models.CharField(max_length=1)
    SDProductCodeLength = models.CharField(max_length=1)
    SDPresetTenths = models.CharField(max_length=1)
    SDTaxFileRateFormat = models.CharField(max_length=1)

    SystemUnitsLong = models.CharField(max_length=10)

    FeeMethod = models.CharField(max_length=1)
    FeeTaxRate = models.CharField(max_length=10)
    FeeTaxDescription = models.CharField(max_length=100)
    FeeTaxStorage = models.CharField(max_length=1)

    Fee1Description = models.CharField(max_length=100)
    Fee1TaxMethod = models.CharField(max_length=1)
    Fee2Description = models.CharField(max_length=100)
    Fee2TaxMethod = models.CharField(max_length=1)
    Fee3Description = models.CharField(max_length=100)
    Fee3TaxMethod = models.CharField(max_length=1)

    Fee1Enabled = models.CharField(max_length=1)
    Fee1Amount = models.CharField(max_length=10)
    Fee2Enabled = models.CharField(max_length=1)
    Fee2Amount = models.CharField(max_length=10)
    Fee3Enabled = models.CharField(max_length=1)
    Fee3Amount = models.CharField(max_length=10)
    
    TaxPercentDescription = models.CharField(max_length=100)
    TaxDollarsDescription = models.CharField(max_length=100)

    DiscountASource = models.CharField(max_length=1)
    DiscountAEnabled = models.CharField(max_length=1)
    DiscountBSource = models.CharField(max_length=1)
    DiscountBEnabled = models.CharField(max_length=1)

    DiscountAType = models.CharField(max_length=1)
    DiscountARate = models.CharField(max_length=10)
    DiscountADays = models.CharField(max_length=10)
    DiscountBType = models.CharField(max_length=1)
    DiscountBRate = models.CharField(max_length=10)

    def __repr__(self):
        return "<Option object: {}>".format(self.user)
    def __str__(self):
        return "<Option object:: {}>".format(self.user)
