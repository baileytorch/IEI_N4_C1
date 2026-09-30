from django.db import models

str_habilitado = "Habilitado"
str_fecha_creacion = "Fecha Creación"
str_fecha_actualizacion = "Fecha Actualización"
str_codigo = "Código"
str_nombre = "Nombre"
str_descripcion = "Descripción"
str_www = "WWW"
str_email = "Email"
str_telefono = "Teléfono"
str_fecha_nac = "Fecha Nacimiento"

class Pais(models.Model):
    nombre = models.CharField("País",max_length=50,null=False)
    nacionalidad = models.CharField("Nacionalidad",max_length=30,null=False)
    iso_2 = models.CharField("ISO 2",max_length=2,null=False)
    iso_3 = models.CharField("ISO 3",max_length=3,null=False)
    habilitado = models.BooleanField(str_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)
    class Meta:
        db_table_comment = "Información de paises del mundo, para asociar a autores y lectores."

class Region(models.Model):
    codigo = models.CharField(str_codigo,max_length=2,null=False)
    region = models.CharField("Región",max_length=30,null=False)
    habilitado = models.BooleanField(str_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)
    class Meta:
        db_table_comment = "Regiones de Chile, data de SUBDERE."

class Provincia(models.Model):
    codigo = models.CharField(str_codigo,max_length=3,null=False)
    provincia = models.CharField("Provincia",max_length=50,null=False)
    region = models.ForeignKey(Region,on_delete=models.CASCADE,null=False)
    habilitado = models.BooleanField(str_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)
    class Meta:
        db_table_comment = "Provincias de Chile, data de SUBDERE. Pertenece a una región específica."

class Comuna(models.Model):
    codigo = models.CharField(str_codigo,max_length=5,null=False)
    comuna = models.CharField("Comuna",max_length=60,null=False)
    provincia = models.ForeignKey(Provincia,on_delete=models.CASCADE,null=False)
    habilitado = models.BooleanField(str_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)
    class Meta:
        db_table_comment = "Comunas de Chile, data de SUBDERE. Pertenece a una provincia específica."

class Direccion(models.Model):
    comuna = models.ForeignKey(Comuna,on_delete=models.CASCADE,null=False)
    calle = models.CharField("Calle",max_length=100,null=True)
    numero = models.CharField("Número",max_length=10,null=True)
    departamento = models.CharField("Dpto/Oficina",max_length=10,null=True)
    habilitado = models.BooleanField(str_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)
    class Meta:
        db_table_comment = "Provincias de Chile, data de SUBDERE. Pertenece a una región específica."

class Biblioteca(models.Model):
    nombre = models.CharField(str_nombre,max_length=50,null=False)
    web = models.URLField(str_www,null=True)
    correo = models.EmailField(str_email,null=True)
    telefono = models.CharField(str_telefono,max_length=15,null=True)
    direccion = models.ForeignKey(Direccion,on_delete=models.CASCADE,null=True)
    habilitado = models.BooleanField(str_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)
    class Meta:
        db_table_comment = "Datos de biblioteca."

class Autor(models.Model):
    nombre = models.CharField(str_nombre,max_length=100,null=False)
    pseudonimo = models.CharField("Pseudónimo",max_length=50,null=True)
    nacionalidad = models.ForeignKey(Pais,on_delete=models.CASCADE,null=True)
    fecha_nacimiento = models.DateField(str_fecha_nac,null=True)
    fecha_defuncion = models.DateField("Fecha Defunción",null=True)
    biografia = models.TextField("Biografía",null=True)
    habilitado = models.BooleanField(str_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)
    class Meta:
        db_table_comment = "Datos de autores asociados a publicaciones/libros."

class Genero(models.Model):
    genero = models.CharField("Género Literario",max_length=30,null=False)
    descripcion = models.CharField(str_descripcion,max_length=255,null=True)
    habilitado = models.BooleanField(str_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)
    class Meta:
        db_table_comment = "Géneros literarios asociados a subgéneros."

class SubGenero(models.Model):
    subgenero = models.CharField("Sub-Género Literario",max_length=30,null=False)
    descripcion = models.CharField(str_descripcion,max_length=255,null=True)
    genero = models.ForeignKey(Genero,on_delete=models.CASCADE,null=False)
    habilitado = models.BooleanField(str_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)
    class Meta:
        db_table_comment = "Subgéneros literarios asociados a publicaciones/libros."

class Editorial(models.Model):
    nombre = models.CharField(str_nombre,max_length=50,null=False)
    web = models.URLField(str_www,null=True)
    correo = models.EmailField(str_email,null=True)
    telefono = models.CharField(str_telefono,max_length=15,null=True)
    direccion = models.ForeignKey(Direccion,on_delete=models.CASCADE,null=True)
    habilitado = models.BooleanField(str_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)
    class Meta:
        db_table_comment = "Datos de empresas encargadas de publicaciones."

class Idioma(models.Model):
    idioma = models.CharField("Idioma",max_length=30,null=False)
    habilitado = models.BooleanField(str_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)
    class Meta:
        db_table_comment = "Data de idiomas para asociar a publicaciones."

class Edicion(models.Model):
    fecha_edicion = models.DateField("Fecha Edición",null=False)
    editorial = models.ForeignKey(Editorial,on_delete=models.CASCADE,null=False)
    idioma = models.ForeignKey(Idioma,on_delete=models.CASCADE,null=False)
    habilitado = models.BooleanField(str_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)
    class Meta:
        db_table_comment = "Data específica de una publicación realizada por una editorial."

class Libro(models.Model):
    titulo = models.CharField("Título",max_length=150,null=False)
    paginas = models.IntegerField("Cantidad Páginas",null=False)
    autor = models.ForeignKey(Autor,on_delete=models.CASCADE,null=False)
    subgenero = models.ForeignKey(SubGenero,on_delete=models.CASCADE,null=False)
    edicion = models.ForeignKey(Edicion,on_delete=models.CASCADE,null=False)
    biblioteca = models.ForeignKey(Biblioteca,on_delete=models.CASCADE,null=False)
    habilitado = models.BooleanField(str_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)
    class Meta:
        db_table_comment = "Data específica de libros publicados pertenecientes a la bilbioteca."

class Estado(models.Model):
    estado = models.CharField("Estado",max_length=30,null=False)
    descripcion = models.CharField(str_descripcion,max_length=255,null=True)
    habilitado = models.BooleanField(str_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)
    class Meta:
        db_table_comment = "Data de estado físico de ejemplares en la biblioteca."

class Ubicacion(models.Model):
    codigo = models.CharField(str_codigo,max_length=15,null=False)
    ubicacion = models.CharField("Ubicación",max_length=50,null=False)
    descripcion = models.CharField(str_descripcion,max_length=255,null=True)
    habilitado = models.BooleanField(str_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)
    class Meta:
        db_table_comment = "Data de ubicación física de ejemplares en la biblioteca."

class Inventario(models.Model):
    libro = models.ForeignKey(Libro,on_delete=models.CASCADE,null=False)
    estado = models.ForeignKey(Estado,on_delete=models.CASCADE,null=False)
    ubicacion = models.ForeignKey(Ubicacion,on_delete=models.CASCADE,null=False)
    gtin = models.CharField("Código Barras",max_length=50,null=False)
    habilitado = models.BooleanField(str_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)
    class Meta:
        db_table_comment = "Copias de un libro disponibles para préstamos en biblioteca."

class Usuario(models.Model):
    nombre = models.CharField(str_nombre,max_length=150,null=False)
    rut = models.CharField("RUT",max_length=12,null=False)
    correo = models.EmailField(str_email,null=True)
    telefono = models.CharField(str_telefono,max_length=15,null=True)
    nacionalidad = models.ForeignKey(Pais,on_delete=models.CASCADE,null=True)
    fecha_nacimiento = models.DateField(str_fecha_nac,null=False)
    contrasenia = models.CharField(max_length=128,null=True)
    direccion = models.ForeignKey(Direccion,on_delete=models.CASCADE,null=True)
    biblioteca = models.ForeignKey(Biblioteca,on_delete=models.CASCADE,null=False)
    habilitado = models.BooleanField(str_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)
    class Meta:
        db_table_comment = "Registro de usuarios de biblioteca."

class Prestamo(models.Model):
    libro = models.ForeignKey(Inventario,on_delete=models.CASCADE,null=False)
    lector = models.ForeignKey(Usuario,on_delete=models.CASCADE,null=False)
    fecha_prestamo = models.DateTimeField("Fecha Préstamo",auto_now_add=True)
    fecha_devolucion = models.DateTimeField("Fecha Devolución",null=False)
    fecha_retorno = models.DateTimeField("Fecha Retorno",null=True)
    class Meta:
        db_table_comment = "Registro de préstamo de libros en la biblioteca."