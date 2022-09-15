from django.contrib.auth.models import User
from rest_framework import serializers

from beers.models import References, Bars, ViewStock, Stock
 
class UserSerializer(serializers.HyperlinkedModelSerializer):
    beers = serializers.HyperlinkedRelatedField(
        many=True, view_name='beer-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'beers')


class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = References
        fields = ['id', 'ref', 'name', 'description']


class BarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bars
        fields = ['id', 'name']


class StocksSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewStock
        fields = ('reference', 'bars', 'stock')


class ViewStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewStock
        fields = ('reference', 'bars', 'stock')
