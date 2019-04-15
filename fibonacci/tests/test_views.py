import unittest
from django.test import TestCase,Client
from django.urls import resolve,reverse

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('fibonacci',args=[78])

    def test_fibonacci_view_GET(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code,200)

if __name__ == '__main__':
    unittest.main()