from . import views
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.aktive_routen, name="aktive_routen"),
    path("aktive_routen/", views.aktive_routen, name="aktive_routen"),
    path("aktive_kunden/", views.aktive_kunden, name="aktive_kunden"),
    path("citygruen/", views.redirect_view, name="redirect_view"),
    path("route/<int:pkRoute>/", views.route_standorte, name="route_standorte"),
    path("route/standort/<int:pkStandort>/", views.standort_pflanzen, name="standort_pflanzen"),
    path("insert_pflanze/", views.new_pflanze, name="insert_pflanze"),
    path("insert_standort/", views.new_standort, name="insert_standort"),
    path("insert_route/", views.new_route, name="insert_route"),
    path("insert_kunde/", views.new_kunde, name="insert_kunde"),
    path("alter_pflanze/", views.alter_pflanze, name="alter_pflanze"),
    path("alter_pflanze/<str:NamePflanze>", views.alter_pflanze_suche, name="alter_pflanze_suche"),
    path("alter_pflanze/<str:NamePflanze>/<str:NrPflanze>", views.alter_pflanze_fuellen, name="alter_pflanze_fuellen"),
    path("alter_kunde/", views.alter_kunde, name="alter_kunde"),
    path("alter_kunde/<str:NameKunde>", views.alter_kunde_suche, name="alter_kunde_suche"),
    path("alter_kunde/<str:NameKunde>/<str:NrKunde>", views.alter_kunde_fuellen, name="alter_kunde_fuellen"),
    path("alter_standort/", views.alter_standort, name="alter_standort"),
    path("alter_standort/<str:NameStandort>", views.alter_standort_suche, name="alter_standort_suche"),
    path("alter_standort/<str:NameStandort>/<str:NrStandort>", views.alter_standort_fuellen, name="alter_standort_fuellen"),
    path("alter_route/", views.alter_route, name="alter_route"),
    path("alter_route/<str:NameRoute>", views.alter_route_suche, name="alter_route_suche"),
    path("alter_route/<str:NameRoute>/<str:NrRoute>", views.alter_route_fuellen, name="alter_route_fuellen"),
    path("zuweisung_routestandort/", views.zuweisung_routestandort, name="zuweisung_routestandort"),
    path("zuweisung_routestandort/<str:NameRoute>", views.zuweisung_routestandort_sucheRoute, name="zuweisung_routestandort_sucheRoute"),
    path("zuweisung_routestandort/<str:NameRoute>/<str:NrRoute>", views.zuweisung_routestandort_fuellenRoute, name="zuweisung_routestandort_fuellenRoute"),
    path("zuweisung_routestandort/<str:NameRoute>/<str:NrRoute>/<str:Zuweisungen>", views.zuweisung_routestandort_zuweisung, name="zuweisung_routestandort_zuweisung"),
    path("zuweisung_standortpflanze/", views.zuweisung_standortpflanze, name="zuweisung_standortpflanze"),
    path("zuweisung_standortpflanze/<str:NameStandort>", views.zuweisung_standortpflanze_sucheStandort, name="zuweisung_standortpflanze_sucheStandort"),
    path("zuweisung_standortpflanze/<str:NameStandort>/<str:NrStandort>", views.zuweisung_standortpflanze_fuellenStandort, name="zuweisung_standortpflanze_fuellenStandort"),
    path("zuweisung_standortpflanze/<str:NameStandort>/<str:NrStandort>/<str:Zuweisungen>", views.zuweisung_standortpflanze_zuweisung, name="zuweisung_standortpflanze_zuweisung"),
]

urlpatterns += staticfiles_urlpatterns()
