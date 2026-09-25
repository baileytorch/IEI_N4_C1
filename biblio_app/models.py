from django.db import models

# Create your models here.
class Categoria(models.Model):
    categoria = models.CharField(name="Categoría",max_length=20,null=False)
    descripcion = models.CharField(name="Descripción",max_length=100,null=True)

class Pais(models.Model):
    nombre = models.CharField(name="País",max_length=60,null=False)
    nacionalidad = models.CharField(name="Nacionalidad",max_length=20,null=False)
    iso_2 = models.CharField(name="ISO 2",max_length=2,null=False)
    iso_3 = models.CharField(name="ISO 3",max_length=3,null=False)

class Autor(models.Model):
    nombre = models.CharField(name="Nombre",max_length=100,null=False)
    pseudonimo = models.CharField(name="Pseudónimo",max_length=50,null=True)
    nacionalidad = models.ForeignKey(Pais,on_delete=models.CASCADE,db_column='nacionalidad')
    fecha_nacimiento = models.DateField(name="Fecha Nacimiento",null=False)
    fecha_defuncion = models.DateField(name="Fecha Defunción",null=True)

class Comuna(models.Model):
    codigo = models.CharField(name="Código",max_length=5,null=False)
    comuna = models.CharField(name="Comuna",max_length=60,null=False)

class Direccion(models.Model):
    comuna = models.ForeignKey(Comuna,on_delete=models.CASCADE,db_column='comuna')
    calle = models.CharField(name="Calle",max_length=100,null=False)
    numero = models.CharField(name="Número",max_length=10,null=True)
    departamento = models.CharField(name="Departamento/Oficina",max_length=10,null=True)

    def __str__(self):
        return f"{self.comuna}, {self.calle}, {self.numero} Depto/Of {self.departamento}"

class Biblioteca(models.Model):
    nombre = models.CharField(max_length=100,null=False)
    web = models.URLField(max_length=254,null=True)
    correo = models.EmailField(null=True)
    telefono = models.CharField(max_length=15,null=True)
    direccion = models.ForeignKey(Direccion,on_delete=models.CASCADE)