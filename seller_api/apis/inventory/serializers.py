from rest_framework import serializers
from seller_api.apis.inventory.models import SellerInventory


class InventorySerializer(serializers.ModelSerializer):

    product_name = serializers.CharField(source='product.name', read_only=True)
    product_image = serializers.CharField(source='product.image', read_only=True)
    product_description = serializers.CharField(source='product.description', read_only=True)

    class Meta:
        model = SellerInventory
        fields = ('stock', 'price', 'product_name', 'product_image', 'product_description')
