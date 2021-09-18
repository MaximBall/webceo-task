from django.test import TestCase
from ..models import Item, ChangePrice
from django.urls import reverse

class ExistItemNameTests(TestCase):
   
    def test_exist_item_name_view(self):
        response = self.client.get('/') 
        items = Item.objects.all()
        self.assertQuerysetEqual(response.context['items'], items)

    def test_equal_item_change_price_view(self):
        response = self.client.get('/history') 
        items = ChangePrice.objects.all()
        self.assertQuerysetEqual(response.context['prices'], items)