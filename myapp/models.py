from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 
from datetime import datetime

class Employee(models.Model):

    user = models.ForeignKey(
        User, verbose_name="Продавец", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.user.username

class Item(models.Model):
    
    name = models.CharField(
        max_length=20, verbose_name="Продукт"
    )

    employe = models.ForeignKey(
        Employee, verbose_name="Продавец", on_delete=models.CASCADE
    )

    price = models.DecimalField(
        max_digits=7, decimal_places=2
    )

    def __str__(self):
        return "Item - {0}, Price - {1}".format(self.name, self.price)


class Sale(models.Model):
    
    item = models.ForeignKey(
        Item, verbose_name="Продукт", on_delete=models.CASCADE
    )

    employe = models.ForeignKey(
        Employee, verbose_name="Продавец", on_delete=models.CASCADE
    )

    count = models.IntegerField()

    total_price = models.DecimalField(
        max_digits=7, decimal_places=2
    )

    price_one_item = models.DecimalField(
        max_digits=7, decimal_places=2
    )

    date_sale = models.DateField(auto_now=True)

    def __str__(self):
        return "Item - {0}, Total price - {1}".format(self.item, self.total_price)

    def get_absolute_url(self):
        return reverse('sales_list')

    def save(self, *args, **kwargs):
        self.employe = self.item.employe
        self.price_one_item = self.item.price
        self.total_price = self.item.price * self.count
        super(Sale, self).save(*args, **kwargs)
    
class ChangePrice(models.Model):
        
    item = models.ForeignKey(
        Item, verbose_name="Продукт", on_delete=models.CASCADE
    )

    date_change = models.DateTimeField(auto_now=True)

    price = models.DecimalField(
        max_digits=7, decimal_places=2
    )

    def __str__(self):
        return "Item - {0}, DateTime update price - {1}".format(self.item, self.date_change)
