from django.test import TestCase
from django.contrib.auth import get_user_model


class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='user@mail.com', username='user1', password='secure',
                                        phone_number='123231321', gender=0)
        self.assertEqual(user.email, 'user@mail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            self.assertIsNotNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password="secure")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email='superuser@mail.com', username='user1', password='secure',
                                                   phone_number='123231321', gender=1)
        self.assertEqual(admin_user.email, 'superuser@mail.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            self.assertIsNotNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='superuser@mail.com', password='secure', is_superuser=False)
