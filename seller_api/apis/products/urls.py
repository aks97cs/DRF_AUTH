from django.conf.urls import url
from seller_api.apis.products.views import ProductList, ProductDetails
URL = [
    url('list', ProductList.as_view(), name='product_list'),
    url('(?P<pk>\w+)', ProductDetails.as_view(), name='product_detail'),
]
