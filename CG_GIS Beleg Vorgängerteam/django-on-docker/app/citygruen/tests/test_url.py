import os
from datetime import *
from django.conf import settings
from django.test import TestCase
from django.urls import resolve, reverse
from citygruen.views import *


class AktiveRoutenPageTest(TestCase):
    def setUp(self):
        pass
    
    def test_aktive_routen_test(self):
        url = reverse('aktive_routen')
        self.assertEqual(resolve(url).func, aktive_routen)

    def test_redirect_view_test(self):
        url = reverse('redirect_view')
        self.assertEqual(resolve(url).func, redirect_view)
    
    def test_insert_pflanze_test(self):
        url = reverse('insert_pflanze')
        self.assertEqual(resolve(url).func, new_pflanze)

    def test_insert_standort_test(self):
        url = reverse('insert_standort')
        self.assertEqual(resolve(url).func, new_standort)
    
    def test_insert_route_test(self):
        url = reverse('insert_route')
        self.assertEqual(resolve(url).func, new_route)

    def test_insert_kunde_test(self):
        url = reverse('insert_kunde')
        self.assertEqual(resolve(url).func, new_kunde)
    
    def test_alter_pflanze_test(self):
        url = reverse('alter_pflanze')
        self.assertEqual(resolve(url).func, alter_pflanze)