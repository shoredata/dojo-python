# Inside models.py
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Dojo(models.Model):
    # the id field is added as auto_increment automatically by django
    # id = models.AutoField(primary_key=True)    
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.TextField(max_length=2)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<Dojo object: {} {} {} {} {}>".format(self.id, self.name, self.city, self.state, self.desc)
class Ninja(models.Model):
    fist_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # # Notice the association made with ForeignKey for a one-to-many relationship
    # # There can be many comments to one blog
    # Since Django 2.x, on_delete is required.
    # Django Documentation
    # Deprecated since version 1.9: on_delete will become a required argument in Django 2.0. In older versions it defaults to CASCADE.
    # dojo_id = models.ForeignKey(Dojo, on_delete=models.CASCADE, related_name = "dojos")
    # https://stackoverflow.com/questions/44160983/what-does-related-name-do
    dojo_id = models.ForeignKey(Dojo, on_delete=models.CASCADE)
    def __repr__(self):
        return "<Comment object: {} {} {} {}>".format(self.id, self.dojo_id, self.first_name, self.last_name)
