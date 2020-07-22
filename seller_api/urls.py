"""seller_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from seller_api.apis.users.urls import URL as USER_URL
from seller_api.apis.products.urls import URL as PRODUCT_URL
from seller_api.apis.inventory.urls import URL as INVENTORY_URL

urlpatterns = [
    path('api/v1/inventory/', include(INVENTORY_URL)),
    path('api/v1/products/', include(PRODUCT_URL)),
    path('api/v1/users/', include(USER_URL)),
    path('admin/', admin.site.urls),
]
