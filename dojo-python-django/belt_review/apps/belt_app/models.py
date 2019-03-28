from __future__ import unicode_literals
from django.db import models

import re
# import bcrypt


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# single-words only
NAME_REGEX = re.compile(r'^[a-zA-Z ]+$')
ALIAS_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+$')
# full name field, multiple words
# FULLNAME_REGEX = re.compile(r'^[_A-z0-9]*((-|\s)*[_A-z0-9])+$)')
PASSWORD_REGEX = re.compile(r'^[a-zA-Z0-9]+$')


# class ReviewManager(models.Manager):
#     def create_validator(self, postData):
#         errors = {}
#         if len(postData['review_text']) <= 1:
#             errors["review_text"] = "Review Text should not be blank"
#         if len(postData['review_text']) > 255:
#             errors["review_textlong"] = "Review should be less than 256 chars"
#         if int(postData['rating']) < 1 or  int(postData['rating']) > 5:
#             errors["rating"] = "Rating must be from 1 to 5"
#         return errors


class BookManager(models.Manager):
    def review_validator(self, postData):
        errors = {}

        # when called from existing book: 
        # <QueryDict: {'csrfmiddlewaretoken': ['mmOVj0H3bg3yQ9K2QI7XU4ryQpD5DsVZAqz3IpGC1n5GSKW3ym3yU5kE87hf8KrZ'], 
        # 'review': ['i want to review this book'], 
        # 'book_id': ['1'], 
        # 'rating': ['5']}>

        if len(postData['review_text']) <= 1:
            errors["review_textshort"] = "Review should not be blank"
        if len(postData['review_text']) > 255:
            errors["review_textlong"] = "Review should be less than 256 chars"
        if "book_id" not in postData:
            if len(postData['book_title']) <= 1:
                errors["book_title"] = "Book Title should not be blank"
            if len(postData['book_title']) > 255:
                errors["book_titlelong"] = "Book Title should be less than 256 chars"
            if len(postData['author_name']) <= 1:
                errors["author_name"] = "Author Name should not be blank"
            if len(postData['author_name']) > 255:
                errors["author_namelong"] = "Author Name should be less than 256 chars"

        return errors

# class AuthorManager(models.Manager):
#     def create_validator(self, postData):
#         errors = {}
#         if len(postData['authorname']) <= 1:
#             errors["authorname"] = "Author should not be blank"
#         return errors


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
        if len(postData['username']) <= 1:
            errors["username1"] = "Name should be more than 1 character"
        if len(postData['username']) > 255:
            errors["username255"] = "Name should be less than 256 characters"
        if not NAME_REGEX.match(postData['username']):   
            errors["usernamechars"] = "Name should be valid characters only"

        if len(postData['useralias']) <= 1:
            errors["useralias1"] = "Alias should be more than 1 character"
        if len(postData['username']) > 255:
            errors["useralias255"] = "Alias should be less than 256 characters"
        if not ALIAS_REGEX.match(postData['useralias']):   
            errors["useraliaschars"] = "Alias should be alpha characters only"

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
    username = models.CharField(max_length=255)
    useralias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    passwordhash_decoded = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

    def __repr__(self):
        return "<User object: {} {} {} {}>".format(self.username, self.useralias, self.email, self.passwordhash_decoded)
    def __str__(self):
        return "<User object:: {} {} {} {}>".format(self.username, self.useralias, self.email, self.passwordhash_decoded)


class Author(models.Model):
    authorname = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # objects = AuthorManager()

    def __repr__(self):
        return "<Author object: {}>".format(self.authorname)
    def __str__(self):
        return "<Author object:: {}>".format(self.authorname)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name = "books")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = BookManager()

    def __repr__(self):
        return "<Book object: {} {}>".format(self.title, self.author)
    def __str__(self):
        return "<Book object:: {} {}>".format(self.title, self.author)

class Review(models.Model):
    review = models.CharField(max_length=255)
    rating = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "reviews")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name = "reviews")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # objects = ReviewManager()
    
    def __repr__(self):
        return "<Review object: {} {} {} {}>".format(self.review, self.rating, self.user, self.book)
    def __str__(self):
        return "<Review object: {} {} {} {}>".format(self.review, self.rating, self.user, self.book)




