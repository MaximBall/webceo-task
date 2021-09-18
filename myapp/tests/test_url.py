from django.test import TestCase


class StatusCodeTests(TestCase):
    
    def test_main_url(self):
       response = self.client.get('/')
       self.assertEqual(response.status_code, 200)

    def test_buy_apple_url(self):
       response = self.client.get('/buy/apple')
       self.assertEqual(response.status_code, 200)

    def test_login_url(self):
       response = self.client.get('/login')
       self.assertEqual(response.status_code, 200)