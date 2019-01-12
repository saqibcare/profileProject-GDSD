# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


# importing for ImageKit django application for resizing of images

# from imagekit.models import ImageSpecField, ProcessedImageField
# from imagekit.processors import ResizeToFill

# Create your models here.
from pip._vendor.pyparsing import _defaultExceptionDebugAction


class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return '%s' % self.title


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

    def __str__(self):
        return '%s' % self.name


class Image(models.Model):
    image = models.FileField(blank=False, null=False, default='DEFAULT VALUE')
    # thumbnail = ProcessedImageField(source='image',
    #                                   upload_to='Thumbnail',
    #                                   processors=[ResizeToFill(100, 50)],
    #                                   format='JPEG',
    #                                   options={'quality': 60})
    displayImage = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Messages(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender_set')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver_set')
    text = models.TextField(max_length=500)
    dateTime = models.DateTimeField(auto_now=True)


class WishList(models.Model):
    product = models.ManyToManyField(Product)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)







