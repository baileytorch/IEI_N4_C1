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
    path('grupo_biblioteca/crear_biblioteca', views.BibliotecaCreateView.as_view(), name='crear_biblioteca'),
    path('grupo_autor/listado_autores', views.AutorListView.as_view(), name='listado_autores'),
    path('grupo_autor/crear_autor', views.AutorCreateView.as_view(), name='crear_autor'),
    path('grupo_autor/<int:pk>/modificar_autor', views.EditarAutor.as_view(), name='modificar_autor'),
    path('grupo_autor/<int:pk>/detalle_autor', views.DetalleAutor.as_view(), name='detalle_autor'),
    path('grupo_autor/<int:pk>/deshabilitar_autor', views.DetalleAutor.as_view(), name='deshabilitar_autor')
]