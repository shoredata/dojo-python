from __future__ import unicode_literals
from django.db import models

import re
# import bcrypt


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^[a-zA-Z0-9]+$')

# Create your models here.

# Show validation error messages if validations fail the following tests
# First Name - Required; No fewer than 2 characters; letters only
# Last Name - Required; No fewer than 2 characters; letters only
# Email - Required; Valid Format
# Password - Required; No fewer than 8 characters in length; matches Password Confirmation


class UserManager(models.Manager):
    def login_validator(self, postData):
        errors = {}
        if len(postData['loginemail']) <= 1:
            errors["email"] = "EMail should be more than 1 character"
        if len(postData['loginpassword']) <= 7:
            errors["password"] = "Password should be more than 7 characters"
        return errors


    def basic_validator(self, postData):
        errors = {}
        if len(postData['firstname']) <= 1:
            errors["firstname1"] = "First Name should be more than 1 character"
        if len(postData['firstname']) > 255:
            errors["firstname255"] = "First Name should be less than 256 characters"
        if not NAME_REGEX.match(postData['firstname']):   
            errors["firstnamechars"] = "First Name should be alpha characters only"

        if len(postData['lastname']) <= 1:
            errors["lastname1"] = "Last Name should be more than 1 character"
        if len(postData['lastname']) > 255:
            errors["lastname255"] = "Last Name should be less than 256 characters"
        if not NAME_REGEX.match(postData['lastname']):   
            errors["lastnamechars"] = "Last Name should be alpha characters only"

        if len(postData['email']) <= 1:
            errors["email1"] = "EMail should be more than 1 character"
        if len(postData['email']) > 255:
            errors["email255"] = "EMail should be less than 256 characters"
        if not EMAIL_REGEX.match(postData['email']):   
            errors["emailchars"] = "EMail format invalid"

        if len(postData['password1']) <= 7:
            errors["password7"] = "Password should be more than 7 characters"
        if len(postData['password1']) > 255:
            errors["password256"] = "Password should be less than 256 characters"
        passw = postData['password1']
        x = False
        while not x:  
            if not re.search("[a-z]",passw):
                errors["passwordlower"] = "Password requires a lowercase letter"
                break
            elif not re.search("[0-9]",passw):
                errors["passwordnum"] = "Password requires a numeric character"
                break
            elif not re.search("[A-Z]",passw):
                errors["passwordupper"] = "Password requires an uppercase letter"
                break
            elif re.search("\s",passw):
                errors["passwordchars"] = "Password contains invalid character(s)"
                break
            else:
                x=True
                break
        return errors


class User(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    passwordhash_decoded = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # *************************
    # Connect an instance of BlogManager to our Blog model overwriting
    # the old hidden objects key with a new one with extra properties!!!
    objects = UserManager()
    # *************************

    def __repr__(self):
        return "<User object: {} {} {} {}>".format(self.firstname, self.lastname, self.email, self.passwordhash_decoded)


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "messages")
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __repr__(self):
        return "<Message object: {} {}>".format(self.user, self.message)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "comments")
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name = "comments")
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __repr__(self):
        return "<Comment object: {} {} {}>".format(self.user, self.message, self.comment)

