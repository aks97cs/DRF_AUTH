from django.db import models
from seller_api.apis.users.models import Seller
from seller_api.apis.products.models import SellerProduct


class SellerInventory(models.Model):
    id = models.UUIDField(editable=False, primary_key=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    product = models.ForeignKey(SellerProduct, on_delete=models.CASCADE)
    stock = models.IntegerField()
    price = models.IntegerField()
    modified = models.DateTimeField(auto_now=True, editable=False)
