from django.dispatch import receiver
from django.db.models.signals import pre_save
from seller_api.apis.inventory.models import SellerInventory
import uuid


@receiver(pre_save, sender=SellerInventory)
def before_save(sender, instance, **kwargs):
    if not instance.id:
        instance.id = uuid.uuid4().hex
