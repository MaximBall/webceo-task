from django.test import TestCase


class StatusCodeTests(TestCase):
    
   def test_index_view_with_no_questions(self):
       response = self.client.get('/')
       self.assertEqual(response.status_code, 200)