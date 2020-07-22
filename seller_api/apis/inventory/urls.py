from django.conf.urls import url
from seller_api.apis.inventory.views import ProductSearch
URL = [
    url('search/(?P<name>\w+)', ProductSearch.as_view(), name='product_search'),
]