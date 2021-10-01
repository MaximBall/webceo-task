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
            # print(resp_items.name, '----', db_items.name)
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
    
    @patch('myapp.views.ChangePrice.objects.create')
    def test_post_save_signal(self, create):
        user = User(username='qwerty', password='13213')
        user.save()
        empl = Employee(user=user)
        empl.save()
        Item.objects.create(
            employe=empl,
            name='apple',
            price=20.00
        )
        self.assertEquals(1, create.call_count)

    def test_html_items(self):
        response = self.client.get('/') 
        self.assertTemplateUsed(response, 'item_list.html') 

class Fixture(TestCase):
        fixtures = ['./fixtures/models_data.json',]

        def test_equal_data_from_fixture(self):
            sale = Sale.objects.get(pk=1)
            self.assertEquals(sale.price_one_item, 40.00)

