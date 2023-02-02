from django.contrib.auth import get_user_model
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
        

