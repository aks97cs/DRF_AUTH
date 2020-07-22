from seller_api.apis.users.views import SellerRegistration, SellerLogin
from django.conf.urls import url

URL = [
    url('register', SellerRegistration.as_view(), name='seller_register'),
    url('login', SellerLogin.as_view(), name='seller_login'),
]
