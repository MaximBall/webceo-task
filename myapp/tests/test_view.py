from django.test import TestCase
from ..models import Item

class ExistItemNameTests(TestCase):
   
   def test_exist_item_name_view(self):
       response = self.client.get('/') 
       items = Item.objects.all()
       self.assertQuerysetEqual(response.context['items'], items)