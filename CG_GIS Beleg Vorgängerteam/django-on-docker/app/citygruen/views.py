from csv import reader
from email.policy import default
#from tkinter import Place
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core import serializers

from .models import Kunde

from .models import Route

from .models import Route_Standort

from .models import Standort

from .models import Standort_Pflanze

from .models import Pflanze

# Create your views here.

# @login_required(login_url='/accounts/login/')
# def citygruen(request):
#     return render(request, "citygruen.html")

# @login_required(login_url='/accounts/login/')
# def route(request):
#     return render(request, "route.html")

def login(request):
    return render(request, "login.html")

@login_required(login_url='/accounts/login/')
def aktive_routen(request):
    Routen = Route.objects.filter(Status=True).order_by("id")
    StandorteUngefiltert = Route_Standort.objects.all()
    Standorte = list()
    for P in StandorteUngefiltert:
            if P.Standort.Status:
                Standorte.append(P)

    return render(request, "aktive_routen.html",{'Routen': Routen,'Standorte': Standorte})

@login_required(login_url='/accounts/login/')
def aktive_kunden(request):
    Kunden = Kunde.objects.filter(Status=True).order_by("id")

    return render(request, "aktive_kunden.html",{'Kunden': Kunden})

@login_required(login_url='/accounts/login/')
def redirect_view(request):
    response = redirect('/aktive_routen/')
    return response

@login_required(login_url='/accounts/login/')
def route_standorte(request, pkRoute):
    VerbindungenRouteStandort = Route_Standort.objects.filter(Route=pkRoute).order_by('Route')
    standorte = list()
    for P in VerbindungenRouteStandort:
            if P.Standort.Status:
                standorte.append(P)

    return render(request, "route_standorte.html",{'VerbindungenRouteStandort': standorte})

@login_required(login_url='/accounts/login/')
def standort_pflanzen(request, pkStandort):
    VerbindungenStandortPflanzen = Standort_Pflanze.objects.filter(Standort=pkStandort).order_by('Pflanze')
    pflanzen = list()
    for P in VerbindungenStandortPflanzen:
            if P.Pflanze.Status:
                pflanzen.append(P)

    return render(request, "standort_planzen.html",{'VerbindungenStandortPflanzen': pflanzen})


#     #Routen = Route.objects.all()
#     #Standorte = Standort.objects.all()
# @login_required(login_url='/accounts/login/')
# def route_standorte(request, pkRoute):
#     VerbindungenRouteStandort = Route_Standort.objects.filter(key1=pkRoute).order_by('key2')

#     return render(request, "route_standorte.html",{'VerbindungenRouteStandort': VerbindungenRouteStandort})



# @login_required(login_url='/accounts/login/')
# def standort_planzen(request, pkStandort):
#     VerbindungenStandortPflanzen = Standort_Pflanze.objects.filter(key1=pkStandort).order_by('key2')

#     return render(request, "standort_planzen.html",{'VerbindungenStandortPflanzen': VerbindungenStandortPflanzen})


# @login_required(login_url='/accounts/login/')
# def test(request):
#     Routen = Route.objects.all()
#     return render(request, "test.html",{'Routen': Routen})

# @login_required(login_url='/accounts/login/')    
# def search_nav(request):
#     return render(request, "search_nav.html")


### INSERT FUNKTIONEN

@login_required(login_url='/accounts/login/')
@staff_member_required
def new_pflanze(request):
    """
    Add a application to be voted as a special position to the database, with the variables
    extracted out of the post request and the flag 0 for "application arrived".
    Arguments:
    request(WSGIRequest): The request given to the view by the url configuration
    on which file to be rendered.
    """
    if request.method == 'GET':
        return render(request, "insert_pflanze.html")

    if request.method == 'POST':
        #id = 4
        name = request.POST.get('Name_Pflanze')
        # set the date as the current systemdate
        gattung = request.POST.get('Gattung_Pflanze')
        # title of the application
        pflegehinweis = request.POST.get('Pflegehinweis_Pflanze')
        # office the request is pointet to
        picture = request.POST.get('Picture_Pflanze') #'R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==' 
        # contact data of the applicant
        statusBefore = request.POST.get('Status_Pflanze') #True
        if statusBefore == 'on':
            status = True 
        else:
            status = False
        # initialize the object with the vars
        #new_pfl = Pflanze(id, name, gattung, pflegehinweis, picture, status)
        new_pfl = Pflanze(Name=name, Gattung=gattung, Pflegehinweis=pflegehinweis, Picture=picture, Status=status)

        # save it to the database with django method save
        new_pfl.save()
    return render(request, "insert_pflanze.html")


@login_required(login_url='/accounts/login/')
@staff_member_required
def new_standort(request):

    if request.method == 'GET':
        return render(request, "insert_standort.html")

    if request.method == 'POST':
        name = request.POST.get('Name_Standort') 
        beschreibung = request.POST.get('Beschreibung_Standort')
        adresse = request.POST.get('Adresse_Standort')
        plz = request.POST.get('Postleitzahl_Standort')
        ort = request.POST.get('Ort_Standort')
        latitude = request.POST.get('Latitude_Standort')
        longitude = request.POST.get('Longitude_Standort')
        kundenidausinput = request.POST.get('KundenID_Standort') #integer zahl die eingetragen wird
        kundenid = Kunde.objects.filter(id=kundenidausinput).first()
        statusBefore = request.POST.get('Status_Standort') #True
        if statusBefore == 'on':
            status = True 
        else:
            status = False

        new_std = Standort(Name=name, Beschreibung=beschreibung, Adresse=adresse, PLZ = plz, Ort=ort, 
                            Latitude=latitude, Longitude=longitude, KundenID = kundenid, Status=status)

        new_std.save()
    return render(request, "insert_standort.html")


@login_required(login_url='/accounts/login/')
@staff_member_required
def new_kunde(request):

    if request.method == 'GET':
        return render(request, "insert_kunde.html")

    if request.method == 'POST':
        name = request.POST.get('Name_Kunde') 
        adresse = request.POST.get('Adresse_Kunde')
        plz = request.POST.get('Postleitzahl_Kunde')
        ort = request.POST.get('Ort_Kunde')
        telefonnummer = request.POST.get('Telefonnummer_Kunde')
        email = request.POST.get('Email_Kunde')
        statusBefore = request.POST.get('Status_Kunde')
        if statusBefore == 'on':
            status = True 
        else:
            status = False

        new_knd = Kunde(Name=name, Adresse=adresse, PLZ = plz, Ort=ort, 
                            Telefonnummer=telefonnummer, eMail=email, Status=status)

        new_knd.save()
    return render(request, "insert_kunde.html")


@login_required(login_url='/accounts/login/')
@staff_member_required
def new_route(request):

    if request.method == 'GET':
        return render(request, "insert_route.html")

    if request.method == 'POST':
        name = request.POST.get('Name_Route') 
        beschreibung = request.POST.get('Beschreibung_Route')
        pflegetrupp = request.POST.get('Pflegetrupp_Route')
        statusBefore = request.POST.get('Status_Route') #True
        if statusBefore == 'on':
            status = True 
        else:
            status = False

        new_rte = Route(Name=name, Beschreibung=beschreibung, Pflegetrupp=pflegetrupp, Status=status)

        new_rte.save()
    return render(request, "insert_route.html")

### ALTER FUNKTIONEN


# Pflanze
@login_required(login_url='/accounts/login/')
@staff_member_required
def alter_pflanze(request):

    Pflanzen = Pflanze.objects.all().order_by('id')

    return render(request, "alter_pflanze.html",{'Pflanzen': Pflanzen})

@login_required(login_url='/accounts/login/')
@staff_member_required
def alter_pflanze_suche(request, NamePflanze):

    Pflanzen = Pflanze.objects.filter(Name__contains = NamePflanze).order_by('id')

    return render(request, "alter_pflanze.html",{'Pflanzen': Pflanzen})

@login_required(login_url='/accounts/login/')
@staff_member_required
def alter_pflanze_fuellen(request, NamePflanze, NrPflanze):

    if request.method == 'GET':
        Pflanzen = Pflanze.objects.filter(id = NrPflanze).order_by('id')
        return render(request, "alter_pflanze.html",{'Pflanzen': Pflanzen})

    if request.method == 'POST':
        Id = request.POST.get('ID_Pflanze')
        name = request.POST.get('Name_Pflanze')
        # set the date as the current systemdate
        gattung = request.POST.get('Gattung_Pflanze')
        # title of the application
        pflegehinweis = request.POST.get('Pflegehinweis_Pflanze')
        # office the request is pointet to
        picture = request.POST.get('Picture_Pflanze') #'R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==' 
        # contact data of the applicant
        statusBefore = request.POST.get('Status_Pflanze') #True
        if statusBefore == 'on':
            status = True 
        else:
            status = False
        # initialize the object with the vars
        #new_pfl = Pflanze(id, name, gattung, pflegehinweis, picture, status)
        alt_pfl = Pflanze(id=Id, Name=name, Gattung=gattung, Pflegehinweis=pflegehinweis, Picture=picture, Status=status)

        # save it to the database with django method save
        alt_pfl.save()
    return render(request, "alter_pflanze.html")


#Kunde
@login_required(login_url='/accounts/login/')
@staff_member_required
def alter_kunde(request):

    Kunden = Kunde.objects.all().order_by('id')

    return render(request, "alter_kunde.html",{'Kunden': Kunden})

@login_required(login_url='/accounts/login/')
@staff_member_required
def alter_kunde_suche(request, NameKunde):

    Kunden = Kunde.objects.filter(Name__contains = NameKunde).order_by('id')

    return render(request, "alter_kunde.html",{'Kunden': Kunden})

@login_required(login_url='/accounts/login/')
@staff_member_required
def alter_kunde_fuellen(request, NameKunde, NrKunde):

    if request.method == 'GET':
        Kunden = Kunde.objects.filter(id = NrKunde).order_by('id')
        return render(request, "alter_kunde.html",{'Kunden': Kunden})

    if request.method == 'POST':
        Id = request.POST.get('ID_Kunde')
        name = request.POST.get('Name_Kunde') 
        adresse = request.POST.get('Adresse_Kunde')
        plz = request.POST.get('Postleitzahl_Kunde')
        ort = request.POST.get('Ort_Kunde')
        telefonnummer = request.POST.get('Telefonnummer_Kunde')
        email = request.POST.get('Email_Kunde')
        statusBefore = request.POST.get('Status_Kunde')
        if statusBefore == 'on':
            status = True 
        else:
            status = False

        alt_knd = Kunde(id=Id, Name=name, Adresse=adresse, PLZ = plz, Ort=ort, 
                            Telefonnummer=telefonnummer, eMail=email, Status=status)

        alt_knd.save()
    return render(request, "alter_kunde.html") 


#Standort
@login_required(login_url='/accounts/login/')
@staff_member_required
def alter_standort(request):

    Standorte = Standort.objects.all().order_by('id')

    return render(request, "alter_standort.html",{'Standorte': Standorte})

@login_required(login_url='/accounts/login/')
@staff_member_required
def alter_standort_suche(request, NameStandort):

    Standorte = Standort.objects.filter(Name__contains = NameStandort).order_by('id')

    return render(request, "alter_standort.html",{'Standorte': Standorte})

@login_required(login_url='/accounts/login/')
@staff_member_required
def alter_standort_fuellen(request, NameStandort, NrStandort):

    if request.method == 'GET':
        Standorte = Standort.objects.filter(id = NrStandort).order_by('id')
        return render(request, "alter_standort.html",{'Standorte': Standorte})

    if request.method == 'POST':
        Id = request.POST.get('ID_Standort')
        name = request.POST.get('Name_Standort') 
        beschreibung = request.POST.get('Beschreibung_Standort')
        adresse = request.POST.get('Adresse_Standort')
        plz = request.POST.get('Postleitzahl_Standort')
        ort = request.POST.get('Ort_Standort')
        latitude = request.POST.get('Latitude_Standort')
        longitude = request.POST.get('Longitude_Standort')
        kundenidausinput = request.POST.get('KundenID_Standort') #integer zahl die eingetragen wird
        kundenid = Kunde.objects.filter(id=kundenidausinput).first()
        statusBefore = request.POST.get('Status_Standort') 
        if statusBefore == 'on':
            status = True 
        else:
            status = False

        new_std = Standort(id=Id, Name=name, Beschreibung=beschreibung, Adresse=adresse, PLZ = plz, Ort=ort, 
                            Latitude=latitude, Longitude=longitude, KundenID = kundenid, Status=status)

        new_std.save()
    return render(request, "alter_standort.html")


#Route
@login_required(login_url='/accounts/login/')
@staff_member_required
def alter_route(request):

    Routen = Route.objects.all().order_by('id')

    return render(request, "alter_route.html",{'Routen': Routen})

@login_required(login_url='/accounts/login/')
@staff_member_required
def alter_route_suche(request, NameRoute):

    Routen = Route.objects.filter(Name__contains = NameRoute).order_by('id')

    return render(request, "alter_route.html",{'Routen': Routen})

@login_required(login_url='/accounts/login/')
@staff_member_required
def alter_route_fuellen(request, NameRoute, NrRoute):

    if request.method == 'GET':
        Routen = Route.objects.filter(id = NrRoute).order_by('id')
        return render(request, "alter_route.html",{'Routen': Routen})

    if request.method == 'POST':
        Id = request.POST.get('ID_Route')
        name = request.POST.get('Name_Route') 
        beschreibung = request.POST.get('Beschreibung_Route')
        pflegetrupp = request.POST.get('Pflegetrupp_Route')
        statusBefore = request.POST.get('Status_Route') 
        if statusBefore == 'on':
            status = True 
        else:
            status = False

        alt_rte = Route(id=Id, Name=name, Beschreibung=beschreibung, Pflegetrupp=pflegetrupp, Status=status)

        alt_rte.save()
    return render(request, "alter_route.html")


### ZUWEISUNGS FUNKTIONEN


# Route-Standort
@login_required(login_url='/accounts/login/')
@staff_member_required
def zuweisung_routestandort(request):

    Routen = Route.objects.all().order_by('id')
    Standorte = Standort.objects.all().order_by('id')
    return render(request, "zuweisung_routestandort.html",{'Routen': Routen, 'Standorte': Standorte})   

@login_required(login_url='/accounts/login/')
@staff_member_required
def zuweisung_routestandort_sucheRoute(request, NameRoute):

    Routen = Route.objects.filter(Name__contains = NameRoute).order_by('id')
    Standorte = Standort.objects.all().order_by('id')
    return render(request, "zuweisung_routestandort.html",{'Routen': Routen, 'Standorte': Standorte})   


@login_required(login_url='/accounts/login/')
@staff_member_required
def zuweisung_routestandort_fuellenRoute(request, NameRoute, NrRoute):

    if  request.method == 'GET':
        _Route = Route.objects.all().order_by('id')
        Standorte = Standort.objects.all().order_by('id')
        idRoute = Route.objects.filter(id=NrRoute).first()
        Verbindungen = Route_Standort.objects.filter(Route=idRoute).order_by('id')
        return render(request, "zuweisung_routestandort.html",{'Routen': _Route, 'Standorte': Standorte, 'Verbindungen': Verbindungen, 'idRoute': idRoute})  

    if request.method == 'POST':
        routenidausinput = request.POST.get('ID_Route') #integer zahl die eingetragen wird
        ID_Route = Route.objects.filter(id=routenidausinput).first()
        standortidausinput = request.POST.get('ID_Standort') #integer zahl die eingetragen wird
        ID_Standort = Standort.objects.filter(id=standortidausinput).first()
        freitext = 'Test'

        verbindung_rtestd = Route_Standort(Route=ID_Route, Standort=ID_Standort, Freitext=freitext)
        verbindung_rtestd.save()

        html = 'zuweisung_routestandort.html/' + NameRoute + '/' + NrRoute
    return render(request, html)    

@login_required(login_url='/accounts/login/')
@staff_member_required
def zuweisung_routestandort_zuweisung(request, NameRoute, NrRoute, Zuweisungen):
    _zuweisung = Zuweisungen.split('-')
    for z in _zuweisung:
        _elemente = z.split('+')
        freitext = 'Text'
        _route = Route.objects.filter(id=NrRoute).first()
        _standort = Standort.objects.filter(id=_elemente[0]).first()
        Route_Standort_Verbindung = Route_Standort.objects.filter(Route = NrRoute).filter(Standort=_elemente[0]).first()
        if _elemente[1] == 'true':
            if Route_Standort_Verbindung is None:
                verbindung_rtestd = Route_Standort(Route=_route, Standort=_standort, Freitext=freitext)
                verbindung_rtestd.save()
        else: 
            if Route_Standort_Verbindung is not None:
                Route_Standort_Verbindung.delete()

    html = '/zuweisung_routestandort/' + NameRoute + '/' + NrRoute
    return redirect(html) 




# Standort-Pflanze
@login_required(login_url='/accounts/login/')
@staff_member_required
def zuweisung_standortpflanze(request):

    Standorte = Standort.objects.all().order_by('id')
    Pflanzen = Pflanze.objects.all().order_by('id')
    return render(request, "zuweisung_standortpflanze.html",{'Standorte': Standorte, 'Pflanzen': Pflanzen})   

@login_required(login_url='/accounts/login/')
@staff_member_required
def zuweisung_standortpflanze_sucheStandort(request, NameStandort):

    Standorte = Standort.objects.filter(Name__contains = NameStandort).order_by('id')
    Pflanzen = Pflanze.objects.all().order_by('id')
    return render(request, "zuweisung_standortpflanze.html",{'Standorte': Standorte, 'Pflanzen': Pflanzen})   


@login_required(login_url='/accounts/login/')
@staff_member_required
def zuweisung_standortpflanze_fuellenStandort(request, NameStandort, NrStandort):

    if  request.method == 'GET':
        _Standort = Standort.objects.all().order_by('id')
        Pflanzen = Pflanze.objects.all().order_by('id')
        idStandort = Standort.objects.filter(id=NrStandort).first()
        VerbindungenStdPfl = Standort_Pflanze.objects.filter(Standort=idStandort).order_by('id')
        return render(request, "zuweisung_standortpflanze.html",{'Standorte': _Standort, 'Pflanzen': Pflanzen, 'VerbindungenStdPfl': VerbindungenStdPfl, 'idStandort': idStandort})  

    if request.method == 'POST':
        standortidausinput = request.POST.get('ID_Standort') #integer zahl die eingetragen wird
        ID_Standort = Standort.objects.filter(id=standortidausinput).first()
        pflanzeidausinput = request.POST.get('ID_Pflanze') #integer zahl die eingetragen wird
        ID_Pflanze = Pflanze.objects.filter(id=pflanzeidausinput).first()

        verbindung_stdpfl = Standort_Pflanze(Standort=ID_Standort, Pflanze=ID_Pflanze)
        verbindung_stdpfl.save()

        html = 'zuweisung_standortpflanze.html/' + NameStandort + '/' + NrStandort
    return render(request, html)    

@login_required(login_url='/accounts/login/')
@staff_member_required
def zuweisung_standortpflanze_zuweisung(request, NameStandort, NrStandort, Zuweisungen):
    _zuweisung = Zuweisungen.split('-')
    for z in _zuweisung:
        _elemente = z.split('+')
        if _elemente[2] == '':
            anzahl = 0
        else:
            anzahl = _elemente[2]
        _standort = Standort.objects.filter(id=NrStandort).first()
        _pflanze = Pflanze.objects.filter(id=_elemente[0]).first()
        Standort_Pflanze_Verbindung = Standort_Pflanze.objects.filter(Standort = NrStandort).filter(Pflanze=_elemente[0]).first()
        if _elemente[1] == 'true':
            if Standort_Pflanze_Verbindung is None:
                verbindung_stdpfl = Standort_Pflanze(Standort=_standort, Pflanze=_pflanze, Anzahl = anzahl)
                verbindung_stdpfl.save()
            else: 
                _id = Standort_Pflanze_Verbindung.id
                verbindung_stdpfl = Standort_Pflanze(id=_id, Standort=_standort, Pflanze=_pflanze, Anzahl = anzahl)
                verbindung_stdpfl.save()
        else: 
            if Standort_Pflanze_Verbindung is not None:
                Standort_Pflanze_Verbindung.delete()

    html = '/zuweisung_standortpflanze/' + NameStandort + '/' + NrStandort
    return redirect(html)