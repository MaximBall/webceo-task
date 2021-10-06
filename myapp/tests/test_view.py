from django.test import TestCase
from django.urls.base import reverse
from ..models import Item, ChangePrice, Employee, Sale, User
from unittest.mock import patch


class ExistItemNameTests(TestCase):
    fixtures = ['./fixtures/models_data.json',]


    def test_exist_item_name_view(self):
        response = self.client.get('/') 
        items = Item.objects.all()
        for resp_items, db_items in zip(response.context['items'], items):
            self.assertTrue(resp_items.name == db_items.name)
        self.assertQuerysetEqual(response.context['items'], items)
        self.assertTrue(len(response.context['items']) == len(items))
        self.assertTrue(items)

    def test_equal_item_change_price_view(self):
        self.client.login(username='admin', password='admin')
        response = self.client.get('/history/') 
        prices = ChangePrice.objects.all()
        self.assertTrue(prices)
        for resp_price_name, db_price_name in zip(response.context['prices'], prices):
            self.assertTrue(resp_price_name.price == db_price_name.price)        
        self.assertQuerysetEqual(response.context['prices'], prices)
        self.assertTrue(len(response.context['prices']) == len(prices))
    
    def test_post_save_signal(self):
        Item.objects.create(
            employe=Employee.objects.latest('id'),
            name='some_item',
            price=50.00
        )
        item = Item.objects.latest('id')
        item.price = 30.00 
        item.save()
        cp = ChangePrice.objects.latest('id')
        self.assertEquals(cp.price, item.price)

    def test_html_items(self):
        response = self.client.get('/') 
        self.assertTemplateUsed(response, 'item_list.html')