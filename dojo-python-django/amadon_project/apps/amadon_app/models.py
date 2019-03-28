from __future__ import unicode_literals
from django.db import models

# Create your models here.

class ProductManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) <= 5:
            errors["name"] = "Product Name should be more than 5 characters"
        if postData['price'] < 0.00:
            errors["price"] = "Product Price should be >= $0.00"
        return errors


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    ordered_quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # *************************
    # Connect an instance of BlogManager to our Blog model overwriting
    # the old hidden objects key with a new one with extra properties!!!
    objects = ProductManager()
    # *************************

    def __repr__(self):
        return "<Product object: {} {} {}>".format(self.name, self.price, self.ordered_quantity)



