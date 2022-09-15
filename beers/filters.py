from django_filters import rest_framework as filters

from .models import References, ViewStock


class ReferenceFilter(filters.FilterSet):
    id = filters.NumberFilter()
    ref = filters.CharFilter(lookup_expr='icontains')
    name = filters.CharFilter(lookup_expr='icontains')
    description = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = References
        fields = ['id', 'ref', 'name', 'description']


class ViewStockFilter(filters.FilterSet):
    id = filters.NumberFilter()
    reference = filters.CharFilter(lookup_expr='icontains')
    bars = filters.CharFilter(lookup_expr='icontains')
    stock = filters.NumberFilter()

    class Meta:
        model = ViewStock
        fields = ('id', 'reference', 'bars', 'stock')
