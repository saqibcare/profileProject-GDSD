from django.contrib.auth.models import User, Group
from rest_framework import serializers

from api.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'password', 'email', 'groups', 'last_login')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('title',)


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'url', 'name')


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'image', 'product', 'displayImage')


# class LocationSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Location
#         fields = ('id', 'name', 'longitude', 'latitude', 'created', 'modified', 'enabled')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'location', 'postedDate', 'description', 'price', 'status', 'sold', 'category', 'owner')


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Messages
        fields = ('id', 'sender', 'receiver', 'text', 'dateTime')


class WishListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WishList
        fields = ('id', 'product', 'customer')


