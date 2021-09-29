from django.test import TestCase


class StatusCodeTests(TestCase):
    
   def test_main_url(self):
       response = self.client.get('/')
       self.assertEqual(response.status_code, 200)

   def test_buy_apple_url(self):
       response = self.client.get('/buy/apple/')
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
