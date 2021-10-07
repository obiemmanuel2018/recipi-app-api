from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """Test user with an email address"""

        email = 'obiemmanuel2018@gmail.com'
        password = '19891999'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test if the new email of a user is normalized"""
        email = 'emmanuel@EHUK.com'
        user = get_user_model().objects.create_user(
            email=email,
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test create user with no email raises error"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Test for creating new superuser"""

        user = get_user_model().objects.create_superuser(
            'obiemmanuel2018@gmail.com',
            '19891999'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
