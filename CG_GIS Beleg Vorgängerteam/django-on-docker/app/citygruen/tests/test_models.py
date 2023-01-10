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

from citygruen.models import *
from citygruen.views import aktive_routen

    


class KundeModelTest(TestCase):
    def setUpTestData():
        Kunde.objects.create(Name= 'TestUser', Adresse = 'Test', Status=True)

    def test_name_label(self):
        kunde = Kunde.objects.get(id=1)
        field_label = Kunde._meta.get_field('Name').verbose_name
        self.assertEqual(field_label, 'Name')
        
    def test_Adresse_label(self):
        kunde = Kunde.objects.get(id=1)
        field_label = Kunde._meta.get_field('Adresse').verbose_name
        self.assertEqual(field_label, 'Adresse')

    def test_Status_label(self):
        kunde = Kunde.objects.get(id=1)
        field_label = Kunde._meta.get_field('Status').verbose_name
        self.assertEqual(field_label, 'Status')

class RouteModelTest(TestCase):
    def setUpTestData():
        Route.objects.create(Name= 'TestRoute', Pflegetrupp='PT-Dresden-1', Status=True)

    def test_name_label(self):
        route = Route.objects.get(id=1)
        field_label = Route._meta.get_field('Name').verbose_name
        self.assertEqual(field_label, 'Name')
    
    def test_pflegetrupp(self):
        route = Route.objects.get(id=1)
        field_label = Route._meta.get_field('Pflegetrupp').verbose_name
        self.assertEqual(field_label, 'Pflegetrupp')

    def test_Status_label(self):
        route = Route.objects.get(id=1)
        field_label = Route._meta.get_field('Status').verbose_name
        self.assertEqual(field_label, 'Status')

class PflanzeModelTest(TestCase):
    def setUpTestData():
        Pflanze.objects.create(Name= 'TestPflanze', Status=True)

    def test_name_label(self):
        pflanze = Pflanze.objects.get(id=1)
        field_label = Pflanze._meta.get_field('Name').verbose_name
        self.assertEqual(field_label, 'Name')
    
    def test_Status_label(self):
        pflanze = Pflanze.objects.get(id=1)
        field_label = Pflanze._meta.get_field('Status').verbose_name
        self.assertEqual(field_label, 'Status')

class StandortModelTest(TestCase):
    def setUpTestData():
        kunde=Kunde.objects.create(Name= 'TestUser', Adresse = 'Test', Status=True)
        Standort.objects.create(Name= 'TestStandort',Latitude=17, Longitude=58, KundenID=kunde,  Status=True)

    def test_name_label(self):
        standort = Standort.objects.get(id=3)
        field_label = Standort._meta.get_field('Name').verbose_name
        self.assertEqual(field_label, 'Name') 

    def test_latitude_label(self):
        standorttest = Standort.objects.get(id=3)
        field_label = Standort._meta.get_field('Latitude').verbose_name
        self.assertEqual(field_label, 'Latitude')
    
    def test_longitude_label(self):
        standorttest = Standort.objects.get(id=3)
        field_label = Standort._meta.get_field('Longitude').verbose_name
        self.assertEqual(field_label, 'Longitude')
    
    def test_ForeignKey_Kunde(self):
        standorttest = Standort.objects.get(id=3)
        self.assertEqual(standorttest.KundenID.Name, 'TestUser')

class Route_Standort_ModelTest(TestCase):
    def setUpTestData():
        kunde=Kunde.objects.create(Name= 'TestUser', Adresse = 'Test', Status=True)
        standort_2= Standort.objects.create(Name= 'TestStandort',Latitude=15, Longitude=60, KundenID=kunde,  Status=True)
        route = Route.objects.create(Name= 'TestRoute', Pflegetrupp='PT-Dresden-1', Status=True)
        Route_Standort.objects.create(Route = route, Standort = standort_2)

    def test_ForeignKey_Route(self):
        route_standort = Route_Standort.objects.get(id=1)
        self.assertEqual(route_standort.Route.Name, 'TestRoute')
    
    def test_ForeignKey_Standort(self):
        route_standort = Route_Standort.objects.get(id=1)
        self.assertEqual(route_standort.Standort.Name, 'TestStandort')
     
class Standort_Pflanze_ModelTest(TestCase):
    def setUpTestData():
        kunde=Kunde.objects.create(Name= 'TestUser', Adresse = 'Test', Status=True)
        standort= Standort.objects.create(Name= 'TestStandort',Latitude=15, Longitude=60, KundenID=kunde,  Status=True)
        pflanze= Pflanze.objects.create(Name= 'TestPflanze', Status=True)
        Standort_Pflanze.objects.create(Standort = standort, Pflanze = pflanze, Anzahl = 3)

    def test_ForeignKey_Pflanze(self):
         standort_pflanze = Standort_Pflanze.objects.get(id=1)
         self.assertEqual(standort_pflanze.Pflanze.Name, 'TestPflanze')

    def test_ForeignKey_Standort(self):
        standort_pflanze = Standort_Pflanze.objects.get(id=1)
        self.assertEqual(standort_pflanze.Standort.Name, 'TestStandort')

    def test_anzahl_label(self):
        standort_pflanze = Standort_Pflanze.objects.get(id=1)
        field_label = standort_pflanze._meta.get_field('Anzahl').verbose_name
        self.assertEqual(field_label, 'Anzahl')

class Wassergaenge_ModelTest(TestCase):
    def setUpTestData():
        kunde=Kunde.objects.create(Name= 'TestUser', Adresse = 'Test', Status=True)
        standort= Standort.objects.create(Name= 'TestStandort',Latitude=15, Longitude=60, KundenID=kunde,  Status=True)
        Wasergeange.objects.create(Standort = standort, Datum = '2022-04-22')

    def test_ForeignKey_Standort(self):
        wassergaenge = Wasergeange.objects.get(id=1)
        self.assertEqual(wassergaenge.Standort.Name, 'TestStandort')
    
    def test_Datum_label(self):
        wassergaenge = Wasergeange.objects.get(id=1)
        field_label = wassergaenge._meta.get_field('Datum').verbose_name
        self.assertEqual( field_label,'Datum')
    
class Pflegegaenge_ModelTest(TestCase):
    def setUpTestData():
        kunde=Kunde.objects.create(Name= 'TestUser', Adresse = 'Test', Status=True)
        standort= Standort.objects.create(Name= 'TestStandort',Latitude=15, Longitude=60, KundenID=kunde,  Status=True)
        Pflegegaenge.objects.create(Standort = standort, Datum = ('2022-04-22'))
    
    def test_ForeignKey_Standort(self):
        pflegegaenge = Pflegegaenge.objects.get(id=1)
        self.assertEqual(pflegegaenge.Standort.Name, 'TestStandort')

    def test_Datum_label(self):
        pflegegaenge = Pflegegaenge.objects.get(id=1)
        field_label = pflegegaenge._meta.get_field('Datum').verbose_name
        self.assertEqual( field_label,'Datum')


    
   
   