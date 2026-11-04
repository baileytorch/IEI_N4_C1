from django.urls import path,include
from rest_framework import routers
from biblio_app import views

enrutador = routers.DefaultRouter()

enrutador.register(r'paises', views.PaisViewSet)
enrutador.register(r'regiones', views.RegionViewSet)
enrutador.register(r'provincias', views.ProvinciaViewSet)
enrutador.register(r'comunas', views.ComunaViewSet)

urlpatterns = [
    path('',include(enrutador.urls)),
    path('grupo_region/listado_regiones', views.RegionListView.as_view(), name='listado_regiones'),
    path('grupo_pais/listado_paises', views.PaisListView.as_view(), name='listado_paises'),
    path('grupo_biblioteca/listado_bibliotecas', views.BibliotecaListView.as_view(), name='listado_bibliotecas'),
    path('grupo_biblioteca/crear_biblioteca', views.BibliotecaCreateView.as_view(), name='crear_biblioteca')
]