from django.test import TestCase
from ..models import Item, ChangePrice, Employee, User
from django.urls import reverse
from django.test.client import Client


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
    
    def test_correctness_data_change_price(self):
        c = Client()
        response = c.post('/admin/myapp/item/add/', {
            'name': 'new-apple',
            'employe': 'admin',
            'price': '40.00'
        })
        self.assertEqual(response.status_code, 302)
        