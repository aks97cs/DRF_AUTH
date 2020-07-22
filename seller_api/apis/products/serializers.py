from rest_framework import serializers
from seller_api.apis.products.models import SellerProduct


class SellerProductSerializer(serializers.ModelSerializer):

    """ we can validate and serialize the field as id """
    id = serializers.UUIDField(format='hex')

    class Meta:
        model = SellerProduct
        fields = ('id', 'name', 'sku_code', 'image', 'description',)
