from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import get_object_or_404
from django_filters import rest_framework as filters

from rest_framework import permissions, renderers, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from .filters import ReferenceFilter

from beers.models import References, Bars,   ViewStock
from beers.permissions import IsAdminUser
from beers.serializers import UserSerializer, ReferenceSerializer, BarSerializer, StocksSerializer
from .pagination import CustomPagination
from .filters import ViewStockFilter


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ReferenceViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving references.
    """
    queryset = References.objects.all()
    serializer_class = ReferenceSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ReferenceFilter

    def list(self, request):
        queryset = References.objects.all()
        serializer_context = {
            'request': request,
        }
        serializer = ReferenceSerializer(
            queryset, many=True, context=serializer_context)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = References.objects.all()
        reference = get_object_or_404(queryset, pk=pk)
        serializer = ReferenceSerializer(reference)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        reference = self.get_object(pk)
        serializer = ReferenceSerializer(reference, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        reference = self.get_object(pk)
        reference.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BarsViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving bars.
    """

    queryset = Bars.objects.all()
    serializer_class = BarSerializer

    permission_classes = (
        permissions.IsAdminUser,)


class StockViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for listing or retrieving stocks.
    """

    serializer_class = StocksSerializer
    queryset = ViewStock.objects.all()
    permission_classes = [IsAdminUser]
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ['id', 'reference', 'bars', 'stock']
    filterset_class = ViewStockFilter
