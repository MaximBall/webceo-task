from django.test import TestCase
from ..models import Item, ChangePrice, Employee, User
from ..views import change_price_item


class ExistItemNameTests(TestCase):
   
    def test_exist_item_name_view(self):
        response = self.client.get('/') 
        items = Item.objects.all()
        for resp_items, db_items in zip(response.context['items'], items):
            self.assertTrue(resp_items.name == db_items.name)
        self.assertQuerysetEqual(response.context['items'], items)
        self.assertTrue(len(response.context['items']) == len(items))

    def test_equal_item_change_price_view(self):
        response = self.client.get('/history/') 
        prices = ChangePrice.objects.all()
        for resp_price_name, db_price_name in zip(response.context['prices'], prices):
            self.assertTrue(resp_price_name.price == db_price_name.price)        
        self.assertQuerysetEqual(response.context['prices'], prices)
        self.assertTrue(len(response.context['prices']) == len(prices))

    def test_change_price(self):
        user = User(username='qwerty', password='13213')
        user.save()
        empl = Employee(user=user)
        empl.save()
        item = Item(employe=empl, name='apple', price=20.00)
        item.save()
        ch_price = change_price_item(item)
        self.assertTrue(item.price == ch_price.price)
        