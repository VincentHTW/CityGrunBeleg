from django.conf import settings
from django.test import TestCase
from django.contrib.auth.password_validation import validate_password


class CGConfigTest(TestCase):
    def test_secret_key_is_secure(self):
        SECRET_KEY = settings.SECRET_KEY
        self.assertEqual(SECRET_KEY, settings.SECRET_KEY)
        is_strong = validate_password(SECRET_KEY)