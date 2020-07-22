from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from seller_api.apis.products.serializers import SellerProductSerializer
from seller_api.apis.products.models import SellerProduct
from rest_framework.permissions import IsAuthenticated
from django.http import Http404


class ProductList(APIView):

    permission_classes = [IsAuthenticated]
    """ listing all products """
    def get(self, request, **kwargs):
        _products = SellerProduct.objects.all()
        serializer = SellerProductSerializer(_products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductDetails(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return SellerProduct.objects.get(pk=pk)
        except SellerProduct.DoesNotExist:
            raise Http404

    """ Fetching product detail by id"""
    def get(self, request, **kwargs):
        _product = self.get_object(pk=kwargs.get('pk'))
        serializer = SellerProductSerializer(_product)
        return Response(serializer.data, status=status.HTTP_200_OK)

