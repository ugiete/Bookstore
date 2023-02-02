from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from django.test import TestCase

from .views import SignUpPageView
from .forms import UserCreationForm

class UserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()

        new_user = User.objects.create_user(
            username='newUser', email='user@ugiete.com', password='P4ssw0rd'
        )

        self.assertEqual(new_user.username, 'newUser')
        self.assertEqual(new_user.email, 'user@ugiete.com')
        self.assertTrue(new_user.is_active)
        self.assertFalse(new_user.is_staff)
        self.assertFalse(new_user.is_superuser)
    
    def test_create_superuser(self):
        User = get_user_model()

        new_admin = User.objects.create_superuser(
            username='newAdmin', email='admin@ugiete.com', password='P4ssw0rd'
        )

        self.assertEqual(new_admin.username, 'newAdmin')
        self.assertEqual(new_admin.email, 'admin@ugiete.com')
        self.assertTrue(new_admin.is_active)
        self.assertTrue(new_admin.is_staff)
        self.assertTrue(new_admin.is_superuser)
        
class SignUpPageTests(TestCase):
    def setUp(self):
        url = reverse("signup")
        self.response = self.client.get(url)

    def test_location(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_template(self):
        self.assertTemplateUsed(self.response, 'registration/signup.html')
        self.assertContains(self.response, "Sign Up")
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")

    def test_resolver(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, SignUpPageView.as_view().__name__)

    def test_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, UserCreationForm)
        self.assertContains(self.response, "csrfmiddlewaretoken")
