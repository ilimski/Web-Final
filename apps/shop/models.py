from django.contrib.auth.models import User
from django.db import models


class Item(models.Model):
    name = models.CharField('Name', max_length=100)
    sizes = models.CharField('Sizes', max_length=100)
    desc = models.TextField('Description')
    price = models.CharField('Price', max_length=50)
    image = models.ImageField('Image', null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    address = models.CharField('Address', max_length=255)
    promocode = models.CharField('Promocode', max_length=255)
