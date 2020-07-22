from django.db.models.signals import pre_save
from django.dispatch import receiver
from seller_api.apis.products.models import SellerProduct
import uuid


@receiver(pre_save, sender=SellerProduct)
def before_save(sender, instance, **kwargs):
    if not instance.id:
        instance.id = uuid.uuid4().hex
        print("instance.idinstance.idinstance.idinstance.idinstance.id", instance.id)

