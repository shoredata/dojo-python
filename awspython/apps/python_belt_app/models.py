from __future__ import unicode_literals
from django.db import models

import re


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class QuoteManager(models.Manager):
    def create_validator(self, postData):
        errors = {}
        if len(postData['author']) <= 3:
            errors["authorshort"] = "Author must be more than 3 characters"
        if len(postData['author']) > 255:
            errors["authorlong"] = "Author must be less than 256 characters"
        if len(postData['quotetext']) <= 10:
            errors["quotetextshort"] = "Quote must more than 10 characters"
        if len(postData['quotetext']) > 255:
            errors["quotetextlong"] = "Quote must be less than 256 characters"
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
        if len(postData['firstname']) <= 2:
            errors["firstname1"] = "First Name should be more than 2 characters"
        if len(postData['firstname']) > 255:
            errors["firstname255"] = "First Name should be less than 256 characters"

        if len(postData['lastname']) <= 2:
            errors["lastname1"] = "Last Name should be more than 2 characters"
        if len(postData['lastname']) > 255:
            errors["lastname255"] = "Last Name should be less than 256 characters"

        if not EMAIL_REGEX.match(postData['email']):   
            errors["emailchars"] = "EMail format invalid"
        if len(postData['email']) > 255:
            errors["email255"] = "EMail should be less than 256 characters"

        return errors


    def basic_validator(self, postData):
        errors = {}
        if len(postData['firstname']) <= 2:
            errors["firstname1"] = "First Name should be more than 2 characters"
        if len(postData['firstname']) > 255:
            errors["firstname255"] = "First Name should be less than 256 characters"

        if len(postData['lastname']) <= 2:
            errors["lastname1"] = "Last Name should be more than 2 characters"
        if len(postData['lastname']) > 255:
            errors["lastname255"] = "Last Name should be less than 256 characters"

        if not EMAIL_REGEX.match(postData['email']):   
            errors["emailchars"] = "EMail format invalid"
        if len(postData['email']) > 255:
            errors["email255"] = "EMail should be less than 256 characters"

        if len(postData['password1']) <= 7:
            errors["password7"] = "Password should be more than 7 characters"
        if len(postData['password1']) > 255:
            errors["password256"] = "Password should be less than 256 characters"

        # passw = postData['password1']
        # x = False
        # while not x:  
        #     if not re.search("[a-z]",passw):
        #         errors["passwordlower"] = "Password requires a lowercase letter"
        #         break
        #     elif not re.search("[0-9]",passw):
        #         errors["passwordnum"] = "Password requires a numeric character"
        #         break
        #     elif not re.search("[A-Z]",passw):
        #         errors["passwordupper"] = "Password requires an uppercase letter"
        #         break
        #     elif re.search("\s",passw):
        #         errors["passwordchars"] = "Password contains invalid character(s)"
        #         break
        #     else:
        #         x=True
        #         break
        return errors


class User(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    passwordhash_decoded = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

    def __repr__(self):
        return "<User object: {} {} {} {}>".format(self.firstname, self.lastname, self.email, self.passwordhash_decoded)
    def __str__(self):
        return "<User object:: {} {} {} {}>".format(self.firstname, self.lastname, self.email, self.passwordhash_decoded)

class Quote(models.Model):
    author = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "quotes")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = QuoteManager()

    def __repr__(self):
        return "<Quote object: {} {} {}>".format(self.text, self.author, self.user)
    def __str__(self):
        return "<Quote object:: {} {} {}>".format(self.text, self.author, self.user)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "likes")
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE, related_name = "likes")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __repr__(self):
        return "<Quote object: {} {}>".format(self.quote, self.user)
    def __str__(self):
        return "<Quote object:: {} {}>".format(self.quote, self.user)


