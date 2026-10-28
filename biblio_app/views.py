from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import viewsets

from . import models as mod

from . import serializer as ser

# Create your views here.
# inicio es una vista basada en función FBV
def inicio(request):
    return render(request,'inicio.html')

# Creación de vistas basadas en clase
class PaisViewSet(viewsets.ModelViewSet):
    queryset = mod.Pais.objects.all()
    serializer_class = ser.PaisSerializer

class PaisListView(ListView):
    model = mod.Pais
    template_name = 'biblio_app/paises/listado_paises.html'

class RegionViewSet(viewsets.ModelViewSet):
    queryset = mod.Region.objects.all()
    serializer_class = ser.RegionSerializer

class RegionListView(ListView):
    model = mod.Region
    template_name = 'biblio_app/regiones/listado_regiones.html'

class ProvinciaViewSet(viewsets.ModelViewSet):
    queryset = mod.Provincia.objects.all()
    serializer_class = ser.ProvinciaSerializer

class ComunaViewSet(viewsets.ModelViewSet):
    queryset = mod.Comuna.objects.all()
    serializer_class = ser.ComunaSerializer