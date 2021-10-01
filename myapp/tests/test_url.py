from django.test import TestCase
from django.test.client import Client


class StatusCodeTests(TestCase):
    
    def test_main_url(self):
       response = self.client.get('/')
       self.assertEqual(response.status_code, 200)

    def test_buy_apple_url(self):
       response = self.client.get('/sale/new/')
       self.assertEqual(response.status_code, 200)

    def test_login_url(self):
       response = self.client.get('/login/')
       self.assertEqual(response.status_code, 200)

    def test_sales_list_url(self):
       response = self.client.get('/sales/')
       self.assertEqual(response.status_code, 200)
   
    def test_history_price_url(self):
       response = self.client.get('/history/')
       self.assertEqual(response.status_code, 200)
    
    def test_correctness_data_change_price(self):
        c = Client()
        response = c.post('/admin/myapp/item/add/', {
            'name': 'new-apple',
            'employe': 'admin',
            'price': '40.00'
        }, follow=True)
        self.assertEqual(response.status_code, 200)
