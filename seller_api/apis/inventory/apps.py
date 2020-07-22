from django.apps import AppConfig


class InventoryConfig(AppConfig):
    name = 'seller_api.apis.inventory'

    def ready(self):
        try:
            from seller_api.apis.inventory.signals import before_save
        except ImportError as err:
            print(err)  # could use alerting and logging instead of print statement
