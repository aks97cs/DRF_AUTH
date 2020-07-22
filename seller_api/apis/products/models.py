from django.db import models


class SellerProduct(models.Model):
    id = models.UUIDField(editable=False, primary_key=True)
    name = models.CharField(max_length=200)
    sku_code = models.CharField(max_length=200, db_index=True)
    image = models.FileField()
    description = models.TextField()

    def __str__(self):
        return self.name

