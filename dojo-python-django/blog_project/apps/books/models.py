# Inside models.py
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "<Author object: {} {}>".format(self.first_name, self.last_name)
class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(max_length=250)
    authors = models.ManyToManyField(Author, related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "<Book object: {} {}>".format(self.title, self.desc)
