from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from django.test import TestCase

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
    username = 'newuser'
    email = 'newuser@email.com'

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_location(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_template(self):
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')

    def test_form(self):
        get_user_model().objects.create_user(self.username, self.email)

        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
