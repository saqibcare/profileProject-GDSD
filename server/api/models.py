# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Host(models.Model):
    fName = models.CharField(max_length=20)
    lName = models.CharField(max_length=20)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    email = models.EmailField(max_length=254)


class Links(models.Model):
    title = models.CharField(max_length=20)
    url = models.URLField()




