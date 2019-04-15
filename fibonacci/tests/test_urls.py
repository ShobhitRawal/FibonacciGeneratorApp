import unittest
from django.urls import resolve,reverse
from django.test import TestCase
from fibonacci.views import HomeView,Fibonacci

class UrlTests(TestCase):

    def test_root_url_resolves_to_home__view(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, HomeView)

    def test_url_resolves_to_fibonacci_view(self):
        number = 10
        url = reverse('fibonacci',args=[number])
        self.assertEqual(resolve(url).func, Fibonacci)

if __name__ == '__main__':
    unittest.main()