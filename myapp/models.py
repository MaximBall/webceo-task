from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):

    user = models.ForeignKey(
        User, verbose_name="Продавец", on_delete=models.CASCADE
    )

    def __str__(self):
        return "{}".format(self.user)


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
        return "{}".format(self.name)


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

    date_sale = models.DateField()

    def __str__(self):
        return "{}".format(self.item, self.date_sale, self.total_price)

    
class ChangePrice(models.Model):
        
    item = models.ForeignKey(
        Item, verbose_name="Продукт", on_delete=models.CASCADE
    )

    date_change = models.DateTimeField()

    price = models.DecimalField(
        max_digits=7, decimal_places=2
    )

    def __str__(self):
        return "{}".format(self.item, self.date_change)
