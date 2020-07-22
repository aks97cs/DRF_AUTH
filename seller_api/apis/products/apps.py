from django.apps import AppConfig


class ProductsConfig(AppConfig):
    name = 'seller_api.apis.products'

    def ready(self):
        try:
            from seller_api.apis.products.signals import before_save
        except ImportError as err:
            print('err')  # in future use alerting and logging instead of print statement
