from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView

class HomePageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_location(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_template(self):
        self.assertTemplateUsed(self.response, 'home.html')
        self.assertContains(self.response, 'home page')
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')

    def test_resolver(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)

class AboutPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_location(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_template(self):
        self.assertTemplateUsed(self.response, 'about.html')
        self.assertContains(self.response, 'About page')
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')

    def test_resolver(self):
        view = resolve('/about/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)