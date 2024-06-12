from django.db import models

# Create your models here.
# class Catalog(models.Model):
#     category = models.ForeignKey()

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.ImageField()
    available = models.BooleanField(default=False)
    article = models.CharField(max_length=255)
    material = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    characteristics = models.JSONField(default=dict)
    season = models.CharField(max_length=255)
    guide = models.JSONField(default=dict)
    description = models.TextField()
    size = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    color = models.CharField(max_length=255)
    def __str__(self):
        return f'{self.name}'


class ProductInCart(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    session_key = models.CharField(max_length=255)
    amount = models.IntegerField()


