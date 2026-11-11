from django.shortcuts import render
from django.views.generic import ListView, CreateView
from rest_framework import viewsets

from . import models as mod
from . import serializer as ser
from . import forms

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

class BibliotecaListView(ListView):
    model = mod.Biblioteca
    template_name = 'biblio_app/biblioteca/listado_bibliotecas.html'

class BibliotecaCreateView(CreateView):
    model = mod.Biblioteca
    fields = ['nombre', 'web', 'correo', 'telefono']
    template_name = 'biblio_app/biblioteca/crear_biblioteca.html'

class AutorListView(ListView):
    model = mod.Autor
    template_name = 'biblio_app/autor/listado_autores.html'

class AutorCreateView(CreateView):
    model = mod.Autor
    form_class = forms.AutorForm
    template_name = 'biblio_app/autor/crear_autor.html'