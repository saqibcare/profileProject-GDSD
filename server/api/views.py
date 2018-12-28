# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User, Group
from api.serializers import *
from rest_framework import viewsets, filters, generics
from django.shortcuts import render

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    ordering_fields = ('username', 'email')

