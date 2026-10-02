from rest_framework import serializers

from .models import Pais
from .models import Region
from .models import Provincia
from .models import Comuna
from .models import Direccion
from .models import Biblioteca
from .models import Autor
from .models import Genero
from .models import SubGenero
from .models import Editorial
from .models import Idioma
from .models import Edicion
from .models import Libro
from .models import Estado
from .models import Ubicacion
from .models import Inventario
from .models import Usuario
from .models import Prestamo

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fileds = ('__all__')

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fileds = ('__all__')

class ProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provincia
        fileds = ('__all__')

class ComunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fileds = ('__all__')