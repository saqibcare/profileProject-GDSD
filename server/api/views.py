# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User, Group
from api.serializers import *
from rest_framework import viewsets, filters, generics
from django.shortcuts import render
# from django_filters import rest_framework as filters
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly


# Create your views here.
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    ordering_fields = ('username', 'email')


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Product.objects.all().filter(sold=False).order_by('postedDate')
    serializer_class = ProductSerializer
    ordering_fields = ('postedDate',)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('status', 'sold', 'category__title', 'owner__username')


class ImageViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def pre_save(self, obj):
        obj.image = self.request.FILES.get('file')


class MessageViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Messages.objects.all()
    serializer_class = MessageSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('sender__username', 'receiver__username')

# class MessageViewSet(filters.BaseFilterBackend):
#     """
#     Filter that only allows users to see their own objects.
#     """
#     queryset = Messages.objects.all()
#     def filter_queryset(self, request, queryset, view):
#         # queryset = Messages.objects.all()
#         return queryset.filter(owner=request.user)


class WishListViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = 'customer__username'
