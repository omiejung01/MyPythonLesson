from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.CharField(max_length=20)
    product_title = models.CharField(max_length=200)
    product_unit = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.product_id