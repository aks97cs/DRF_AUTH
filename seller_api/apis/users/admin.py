from django.contrib import admin
from seller_api.apis.users.models import SellerGroup, Seller

admin.site.register(SellerGroup)
admin.site.register(Seller)
# Register your models here.
