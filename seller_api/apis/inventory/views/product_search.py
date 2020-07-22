from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from seller_api.apis.inventory.serializers import InventorySerializer
from seller_api.apis.inventory.models import SellerInventory
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from django.db.models import Q


class ProductSearch(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self, key):
        try:
            return SellerInventory.objects.filter(Q(product__name__contains=key) | Q(product__sku_code=key))
        except SellerInventory.DoesNotExist:
            raise Http404

    """ wildcard searching  """
    def get(self, request, **kwargs):
        _matched_list = self.get_object(kwargs.get('name'))
        serializer = InventorySerializer(_matched_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
