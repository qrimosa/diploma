from django.db import models

# Create your models here.
# class Catalog(models.Model):
#     category = models.ForeignKey()

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Назва')
    image = models.ImageField(verbose_name='Зображення')
    def __str__(self):
        return f'{self.name}'
    
class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Назва')
    price = models.IntegerField(verbose_name='Ціна')
    image = models.ImageField(verbose_name='Зображення')
    available = models.BooleanField(default=False, verbose_name='Наявність')
    article = models.CharField(max_length=255, verbose_name='Опис товару')
    material = models.CharField(max_length=255, verbose_name='Матеріал')
    country = models.CharField(max_length=255, verbose_name='Країна')
    characteristics = models.JSONField(default=dict, verbose_name='Характеристики')
    season = models.CharField(max_length=255, verbose_name='Сезон')
    guide = models.JSONField(default=dict, verbose_name='Рекомендації щодо догляду')
    description = models.TextField(verbose_name='Опис')
    size = models.CharField(max_length=255, verbose_name='Розмір')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    color = models.CharField(max_length=255, verbose_name='Колір')
    category = models.ForeignKey(Category, on_delete = models.CASCADE, verbose_name='Категорія')
    def __str__(self):
        return f'{self.name}'


class ProductInCart(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    session_key = models.CharField(max_length=255)
    amount = models.IntegerField()
