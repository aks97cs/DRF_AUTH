from django.contrib import admin
from seller_api.apis.inventory.models import SellerInventory


class AdminSellerProduct(admin.ModelAdmin):

    list_display = ['product', 'stock', 'price']
    """ we can also use our custom filter here a/c to need """
    list_filter = ('price', 'stock', )


admin.site.register(SellerInventory, AdminSellerProduct)
