# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User, Group
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

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
    filter_backends = (filters.OrderingFilter, )
    ordering_fields = ('username', 'email')


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Product.objects.all().filter(sold=False).order_by('postedDate')
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter,)
    ordering_fields = ('price', 'postedDate', 'name')
    filter_fields = ('status', 'sold', 'category__title', 'owner__username')
    search_fields = ('name',)


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




class WishListViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('customer',)


class ProductSortingView(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Product.objects.all().filter(sold=False).order_by('postedDate')
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter,)
    ordering_fields = ('price', 'postedDate', 'name')
    filter_fields = ('status', 'sold', 'category__title', 'owner__username')
    search_fields = ('name',)

   #
   #  def id_list(self, request):
   #      q = self.get_queryset().values('price')
   #
   #      l = Response(list(q))
   #
   # # Swap the elements to arrange in order
   #      for iter_num in range(len(l) - 1, 0, -1):
   #          for idx in range(iter_num):
   #              if l[idx] > l[idx + 1]:
   #                  temp = l[idx]
   #                  l[idx] = l[idx + 1]
   #                  l[idx + 1] = temp
   #
   #      return l #returing sorted list on the base of id
   #
   #  def name_Sort(self, request):
   #      lst = self.get_queryset().values('name')
   #      if not lst:
   #          return []
   #          return (name_Sort([x for x in lst[1:] if x < lst[0]])
   #              + [lst[0]] +
   #              name_Sort([x for x in lst[1:] if x >= lst[0]]))
   #
   #      return lst #done sort here alphabetically order
   #


