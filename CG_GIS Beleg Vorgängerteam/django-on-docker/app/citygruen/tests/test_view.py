import os
from datetime import *
from django.conf import settings
from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template import RequestContext
from django.template.loader import render_to_string
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User

from citygruen.views import aktive_routen

class ViewTest(TestCase):
    def setUpTestData():
        pass

    def test_view_url_login(self):
        response =self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_view_url_logout(self):
        response =self.client.get('/accounts/logout/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/logged_out.html')
   
    def test_view_url_aktive_routen(self):
        response =self.client.get('/aktive_routen/')
        self.assertEqual(response.status_code, 302)
    
    def test_view_url_inert_pflanze(self):
        response =self.client.get('/insert_pflanze/')
        self.assertEqual(response.status_code, 302)

    def test_view_url_insert_standort(self):
        response =self.client.get('/insert_standort/')
        self.assertEqual(response.status_code, 302)

    def test_view_url_insert_route(self):
        response =self.client.get('/insert_route/')
        self.assertEqual(response.status_code, 302)

    def test_view_url_insert_kunde(self):
        response =self.client.get('/insert_kunde/')
        self.assertEqual(response.status_code, 302)