# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from pip._vendor.pyparsing import _defaultExceptionDebugAction


class Category(models.Model):
    title = models.CharField(max_length=200)

    def __Str__(self):
        return str(self.title)


class Product(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    postedDate = models.DateField(auto_now_add=True)
    description = models.TextField(max_length=1000)
    price = models.IntegerField(blank=True)
    STATUS = (
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('DENIED', 'Denied'),
    )
    status = models.CharField(max_length=200, choices=STATUS, default=STATUS[0])
    sold = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __Str__(self):
        return str(self.name)


class Image(models.Model):
    url = models.CharField(max_length=5000)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

#
# class Customer(models.Model):
#     address = models.CharField(required=True, max_length=200)
#     contactNumber = models.TextField(max_length=15)
#
#
# class WishList(models.Model):
#
#
# class Messages(models.Model):






