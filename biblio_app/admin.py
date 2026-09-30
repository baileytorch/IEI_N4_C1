from django.contrib import admin
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

# Register your models here.
admin.site.register(Pais)
admin.site.register(Region)
admin.site.register(Provincia)
admin.site.register(Comuna)
admin.site.register(Direccion)
admin.site.register(Biblioteca)
admin.site.register(Autor)
admin.site.register(Genero)
admin.site.register(SubGenero)
admin.site.register(Editorial)
admin.site.register(Idioma)
admin.site.register(Edicion)
admin.site.register(Libro)
admin.site.register(Estado)
admin.site.register(Ubicacion)
admin.site.register(Inventario)
admin.site.register(Usuario)
admin.site.register(Prestamo)