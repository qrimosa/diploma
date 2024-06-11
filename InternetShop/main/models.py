from django.db import models

# Create your models here.
# class Catalog(models.Model):
#     category = models.ForeignKey()

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.ImageField()
    available = models.BooleanField(default=False)
    description = models.TextField()
    size = models.CharField(max_length=255)


class ProductInCart(models.Model):
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    amount = models.IntegerField()


