from rest_framework import serializers

from .models import Pais, Region, Provincia, Comuna, Direccion
from .models import Biblioteca, Autor, Genero, SubGenero, Editorial, Idioma
from .models import Edicion, Libro, Estado, Ubicacion, Inventario, Usuario, Prestamo

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ('__all__')

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('__all__')

class ProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provincia
        fields = ('__all__')

class ComunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = ('__all__')

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = ('comuna','calle','numero','departamento')