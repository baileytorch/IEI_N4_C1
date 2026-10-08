from django.shortcuts import render
from rest_framework import viewsets

from .models import Pais, Region, Provincia, Comuna

from .serializer import PaisSerializer, RegionSerializer, ProvinciaSerializer, ComunaSerializer

# Create your views here.
# inicio es una vista basada en función FBV
def inicio(request):
    return render(request,'inicio.html')

# Creación de vistas basadas en clase
class PaisViewSet(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer

class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class ProvinciaViewSet(viewsets.ModelViewSet):
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer

class ComunaViewSet(viewsets.ModelViewSet):
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer