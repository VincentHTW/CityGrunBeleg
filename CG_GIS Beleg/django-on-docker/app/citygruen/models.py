from django.db import models
import datetime

# Create your models here.


class Kunde(models.Model):
        Name = models.CharField(max_length=50, null=True)
        Adresse = models.CharField(max_length=255, null=True)
        PLZ  = models.CharField(max_length=5, null=True)
        Ort  = models.CharField(max_length=50, null=True)
        Telefonnummer = models.CharField(max_length=50, null=True)
        eMail = models.CharField(max_length=255, null=True)
        Status = models.BooleanField()


class Route(models.Model):
        Name = models.CharField(max_length=50, null=True)
        Beschreibung = models.CharField(max_length=255, null=True)
        Pflegetrupp = models.CharField(max_length=50, null=True)
        Status = models.BooleanField()


class Standort(models.Model):
        Name = models.CharField(max_length=50, null=True)
        Beschreibung = models.CharField(max_length=255, null=True)
        Adresse = models.CharField(max_length=255, null=True)
        PLZ  = models.CharField(max_length=5, null=True)
        Ort  = models.CharField(max_length=50, null=True)
        Latitude = models.DecimalField(decimal_places=6,max_digits=8)
        Longitude = models.DecimalField(decimal_places=6,max_digits=8)
        KundenID = models.ForeignKey(Kunde, on_delete=models.CASCADE)
        Status = models.BooleanField()

class Pflanze(models.Model):
        Name = models.CharField(max_length=50, null=True)
        Gattung = models.CharField(max_length=50, null=True)
        Pflegehinweis = models.CharField(max_length=255, null=True) 
        Picture = models.TextField(null=True, blank=True)
        Status = models.BooleanField()


class Route_Standort(models.Model):
        Route = models.ForeignKey(Route, on_delete=models.CASCADE)
        Standort = models.ForeignKey(Standort, on_delete=models.CASCADE)
        Freitext = models.CharField(max_length=255, null=True)  


class Standort_Pflanze(models.Model):
        Standort = models.ForeignKey(Standort, on_delete=models.CASCADE)
        Pflanze = models.ForeignKey(Pflanze, on_delete=models.CASCADE)
        Anzahl = models.IntegerField(null=True)
        Freitext = models.CharField(max_length=255, null=True)

class Wasergeange(models.Model):
        Standort = models.ForeignKey(Standort, on_delete=models.CASCADE)
        Datum = models.DateField()

class Pflegegaenge(models.Model):
        Standort = models.ForeignKey(Standort, on_delete=models.CASCADE)
        Datum = models.DateField()