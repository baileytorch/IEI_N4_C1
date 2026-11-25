# IEI_N4_C1

## Clases de Backend con Django

Como buenos desarrolladores, ya debemos tener creado un repositorio para trabajar el código de la aplicación que debemos construir.

- Si no ha trabajado aún con repositorios, he construido una pequeña guía paso a paso que está disponible en sus ambientes de aprendizaje.
- Cada estudiante debe construir un proyecto que se ha asignado con anterioridad. La lista de estudiantes con los proyectos asignados y la descripción de los proyectos, los puede encontrar en su ambiente de aprendizaje.

## Creación de Proyectos con Django

1.  ## Creación de Ambiente Virtual
    - Habiendo creado y clonado nuestro repositorio, abrimos la carpeta contenedora en VS Code.
    - Dentro de este directorio, crearemos un ambiente virtual que mantendrá aislada toda la configuración de nuestro proyecto y su entorno de trabajo.
    - Para lograrlo, iniciaremos un nuevo terminal, estando ubicados en el directorio principal.
    - Para crear el ambiente virtual, ejecutamos el siguiente comando en el terminal:

      ```
      python -m venv nombre_ambiente
      ```

    - _VENV_ es acrónimo de _VIRTUAL ENVIRONMENT_, por lo que debemos entender que creará nuestro ambiente virtual.
    - _nombre_ambiente_ debe ser reemplazado por el nombre que Ud. le quiera dar a su ambiente virtual. Es recomendable que sea corto y descriptivo.
    - Nuestro nuevo ambiente virtual tiene 2 directorios muy importantes:
      - _Libs_: Directorio donde encontraremos las librerías asociadas a nuestro proyecto. Cuando está recién creado, sólo contendrá _PIP_.
      - _Scripts_: Directorio que contiene distintos scripts que serán usados durante el desarrollo, como Activate y deactivate.

2.  ## Activación de Ambiente Virtual
    - Mediante el terminal accedemos al directorio creado anteriormente y a su subdirectorio Scripts, ejecutando el siguiente comando:

      ```
      cd mi_ambiente\Scripts
      ```

    - Para activar el ambiente virtual, necesitamos ejecutar uno de los scripts almacenados en el directorio indicado, mediante el siguiente comando en el terminal:

      ```
      .\Activate
      ```

    - Si no se puede ejecutar el comando por restricciones de seguridad, debemos darle permisos al terminal, mediante el siguiente comando:

      ```
      Set-ExecutionPolicy Bypass -Scope CurrentUser
      ```

    - Habiendo ejecutado este comando, ya deberíamos poder ejecutar el comando _Activate_ y activar nuestro ambiente virtual.
    - Si hemos terminado de trabajar, o debemos cambiarnos de proyecto, necesitamos desactivar el ambiente virtual, para lo que usaremos el siguiente comando:

      ```
      deactivate
      ```

    - Todo lo que haremos a continuación debe ser fuera de este directorio, por lo que debemos salir hasta el directorio principal mediante el siguiente comando:

      ```
      cd..
      ```

    - El comando _cd.._ permite salir de un directorio y ubicarnos en el superior, por lo que deberíamos ejecutarlo 2 veces para llegar al directorio principal, saliendo de _mi_ambiente\Scripts_.

3.  ## Actualización de PIP
    - A pesar de haber generado una instalación del entorno desde cero, no está asegurado que contenga la última versión de PIP, por lo que debemos actualizarlo.
    - Para lograrlo, ejecutamos el siguiente comando en nuestro terminal:

      ```
      python -m pip install --upgrade pip
      ```

4.  ## Instalación de Entorno Django
    - Mediante terminal, estando ubicados en el directorio raíz de la aplicación, ejecutaremos el siguiente comando:

      ```
      pip install django
      ```

    - El comando anterior instaló todas las dependencias necesarias para que Django pueda trabajar, las que deberían haber quedado en _mi_ambiente\Libs_. Estas debieran ser:
      - asgiref.
      - django.
      - sqlparse.
      - tzdata.
    - Ahora crearemos el entorno de trabajo de Django mediante el comando:

      ```
      django-admin startproject motor_django .
      ```

    - No debe olvidar el _PUNTO_ al final del comando, para indicar que el directorio de Django se debe crear en el directorio principal de trabajo.
    - Este comando creó la estructura de archivos de Django con nombre _motor_django_, el que Ud. puede cambiar al que guste. Debemos recordar que debe ser suficientemente descriptivo, por lo que es común usar el acrónimo _drf_ por _Django Rest Framework_.
    - Este directorio contiene los archivos de configuración de Django, dentro de los que tenemos.
      - _settings.py_, contiene configuraciones generales, como la conexión a la base de datos.
      - _urls.py_, contiene las rutas para redirigir las solicitudes _REQUEST_ que lleguen a la aplicación.

5.  ## Creación de la Aplicación
    - A continuación, para crear la aplicación que debemos construir, ejecutaremos el siguiente comando mediante terminal:

      ```
      django-admin startapp mi_aplicacion
      ```

    - El comando anterior creó un nuevo directorio llamado _mi_aplicacion_, igual que en los casos anteriores, este nombre debería ser cambiado por un nombre descriptivo de su aplicación.
    - Dentro de este directorio encontraremos los archivos:
      - _admin.py_: el _rest_framework_ de Django posee una herramienta que podría permitirnos hacer _CRUD_ de nuestro modelo de datos y en este archivo registramos los elementos de nuestro modelo para permitirle realizar este proceso.
      - _apps.py_: Permite definir configuraciones específicas y metadatos de nuestra aplicación.
      - _models.py_: Permite definir el _MODELO DE DATOS_ que soportará nuestra aplicación. Contiene clases que representan tablas de nuestra base de datos y que serán mapeadas por nuestro ORM (Object Relational Mapping).
      - _tests.py_: Acá podremos definir nuestros _TESTS UNITARIOS_ para validar automáticamente la lógica de nuestra aplicación, los modelos y las vistas.
      - _views.py_: Este el núcleo de nuestra aplicación, el _CONTROLADOR_. Acá tendremos la lógica que procesará una solicitud o _REQUEST_ enviada a nuestra APP y enviará la respectiva respuesta o _"RESPONSE"_. Esta estructura de trabajo responde al patrón de diseño _Modelo Vista Controlador_, obteniendo data de los modelos, aplicando la lógica y renderizando una vista para mostrar esa respuesta.
    - Cuando la estructura de archivos de la aplicación ya ha sido generada, podemos iniciar el servidor de la aplicación, ejecutando el siguiente comando en el terminal:

      ```
      python manage.py runserver
      ```

    - Este comando inicia el servidor, el que se carga en la url http://127.0.0.1:8000.

6.  ## Plantillas Base
    Las plantillas base permiten crear un esqueleto de diseño común para todas las páginas de una aplicación, evitando la repetición de código HTML y manteniendo la consistencia visual. Esto se logra creando un archivo HTML base que contiene bloques de contenido dinámico, y luego extendiendo esta plantilla en otras páginas para rellenar esos bloques con contenido específico de cada vista.
    - Dentro del directorio de nuestra aplicación, crearemos un nuevo directorio llamado _templates_, donde pondremos todas las vistas de nuestra aplicación.
    - Crear un archivo HTML de plantilla base en la carpeta _mi_aplicacion/templates_ recién creada, puede llamarse _base.html_.

      ```html
      <!DOCTYPE html>
      <html>
        <head>
          <title>{% block titulo %}Mi sitio{% endblock%}</title>
        </head>

        <body>
          <h1>{% block titulo_encabezado %}Bienvenido{%endblock %}</h1>

          {% block contenido %}

          <p>Contenido por defecto.</p>

          {% endblock %}
        </body>
      </html>
      ```

    - Dentro de la plantilla base, se utilizan etiquetas como `{%block nombre_bloque %}` y `{% endblock %}` para definir áreas de contenido que pueden ser utilizadas en las vistas que heredan de ella.
    - Las vistas extienden desde la plantilla base utilizando la sintaxis `{% extends "plantilla_base.html" %}`.

      ```html
      {% extends "base.html" %} {% block titulo %}Página de Inicio{% endblock %}
      {% block titulo_encabezado %}¡Bienvenido a mi sitio!{%endblock %} {% block
      contenido %}
      <p>Este es el contenido específico de la página de inicio.</p>
      {% endblock %}
      ```

7.  ## Modificando la página de inicio
    - Por defecto cuando iniciamos el servidor, carga una página con información de Django, pero no es lo que debiéramos ver cuando cargamos una aplicación, por lo que cambiaremos la página de inicio.
    - Primero debemos indicarle a Django que el directorio de nuestra aplicación contiene una APP, agregamos nuestra APP a la lista _INSTALLED_APPS_ de _motor_django/settings.py_:

      ```
      INSTALLED_APPS = [
          # apps de django
          'mi_aplicacion',
      ]
      ```

    - Dentro del subdiretorio _mi_aplicacion/templates_ creamos la vista HTML que será renderizada por el método creado anteriormente, la que llamaremos _bienvenida.html_.
    - Dentro de este archivo, pondremos el código HTML de nuestra página de bienvenida.
    - En el archivo _mi_aplicacion/views.py_ generamos el método que renderizará la vista creada:

      ```
      from django.shortcuts import render

      def bienvenida(request):
          return render(request, 'bienvenida.html')
      ```

    - Luego debemos importar las vistas desde nuestra app en _motor_django/urls.py_ y llamar al método que renderizará esa vista:

      ```
      from mi_aplicacion import views

      urlpatterns = [
          path('admin/', admin.site.urls),
          path('', views.bienvenida, name='bienvenida'),
      ]
      ```

    - Esta ruta o _PATH_ recibe 4 argumentos:
      - Ruta(string): Obligatorio. Patrón URL usado para identificar la ruta indicada en la aplicación. En este caso es '', una ruta vacía, o el inicio de nuestra APP, después del nombre del servidor *http://127.0.0.1:8000/*.
      - Vista(function): Obligatorio. Función que se llamará al cargar esa URL en la aplicación, la que debería existir en _mi_aplicacion/views.py_. En este caso llamaremos a la función _bienvenida_.
      - Argumentos(Dictionary): Opcional. Argumentos que se enviarán a nuestra función.
      - name(string): Opcional. Nombre que le daremos a nuestro patrón URL. En este caso lo llamaremos _'bienvenida'_ y de esa forma podemos llamarlo por nombre en la barra de navegación.

    - Cuando iniciemos nuevamente nuestro servidor, debiera cargar la vista recién creada en lugar de la vista Django por defecto.

8.  ## Página de Error 404 Genérica
    - Si python NO encuentra un recurso (página) solicitado, arrojará una página de error con información del servidor, lo que involucra un serio problema de seguridad. Para evitarlo, debemos cargar un página genérica de error, lo que lograremos de la siguiente forma:
      - Deshabilitamos el modo de pruebas de nuestra aplicación en _motor_django/settings.py_:

        ```
        DEBUG = False
        ```

      - Cuando el modo de pruebas se ha deshabilitado, ya no se verá la información del servidor al tratar de cargar un recurso que no existe, sino una página de Django que dice:

        ```
        Not Found
        The requested resource was not found on this server.
        ```

      - Si la aplicación NO esta corriendo en modo de prueba, implica que está en modo productivo, lo que nos debería indicar que nuestro servidor local no debería funcionar. Para resolver esto, debemos AUTORIZAR nuestro servidor local, para permitirle que funcione en modo de producción, modificando _motor_django/settings.py_:

        ```
        ALLOWED_HOSTS = ['localhost','127.0.0.1']
        ```

      - Para que se muestre una página de error creada por nosotros, dentro del directorio _templates_ creado anteriormente, crearemos un archivo _html_ de nombre _404_. Django buscará en este directorio ese archivo y lo cargará al no encontrar un recurso.

9.  ## Manejo de Archivos Estáticos
    Para cargar y usar tus propios archivos estáticos (CSS, JavaScript, imágenes) en Django, sigue estos pasos básicos.
    - Asegúrate de que en tu archivo _motor_django/settings.py_ esté configurado el STATIC_URL y la ruta donde Django buscará los archivos:

      ```
      STATIC_URL = 'static/'

      STATICFILES_DIRS = [
          BASE_DIR / "static",
      ]
      ```

    - Puedes poner tus archivos estáticos en un directorio dentro de tu aplicación o en la carpeta raíz del proyecto, creando un directorio _static_ y dentro de ese directorio, generar las subcarpetas que sean necesarias para mantener el orden del sistema y separar distintos tipos de archivos, teniendo idealmente:
      - css: Para almacenar plantillas de estilo en cascada.
      - js: Para almacenar scripts de JavaScript.
      - images: Para almacenar imágenes usadas dentro de la aplicación.
    - Es significativo podeer trabajar con nuestros archivos estáticos, definir nuestros estilos css, usar nuestras propias imágenes, etc. Pero esto alcanza su verdadero potencial cuando logramos incorporar en nuestra aplicación herramientas/frameworks que nos permiten agregar funcionalidad y potenciar nuestro código, como _BootStrap_, _jQuery_, _jQuery Datatables_, etc. Para lograrlo, seguiremos los siguientes pasos:
      - Buscar el framework a implementar, para descargar sus archivos, generalmente un css y un js.
      - Descarga los archivos necesarios y ponlos en los directorios de estáticos correspondientes.
      - Impleméntalos en tus vistas, idealmente en la plantilla base, para tenerlos disponibles en todas las otras vistas, usando las siguientes etiquetas:
        - `{% load static %}`: Esta etiqueta permite cargar los archivos estáticos en la vista, debe ejecutarse antes que cualquier otra instrucción.
        - `{% static 'images/logo.png' %}`: URL al un archvo estático específico. Las usaremos en etiquetas _Link_ o _Script_ con el atributo _SRC_, como por ejemplo:
          - `<link rel="stylesheet" href="{% static 'css/bootstrap.css' %}">`
          - `<link rel="shortcut icon" href="{% static 'images/logo.png' %}" type="image/x-icon">`
          - `<script src="{% static 'js/bootstrap.bundle.js' %}"></script>`

        Todo esto finalmente se incorpora en la vista de la siguiente forma:

        ```html
        {% load static %}

        <!DOCTYPE html>
        <html lang="es">
          <head>
            <meta charset="UTF-8" />
            <meta
              name="viewport"
              content="width=device-width, initial-scale=1.0"
            />

            {% block titulo %}
            <title>Plantilla</title>
            {% endblock %}

            <link rel="stylesheet" href="{% static 'css/bootstrap.css' %}" />
            <link rel="stylesheet" href="{% static 'css/datatables.css' %}" />

            <link
              rel="shortcut icon"
              href="{% static 'images/logo.png' %}"
              type="image/x-icon"
            />
            {% block estilos %}{% endblock %}

            <script src="{% static 'js/bootstrap.bundle.js' %}"></script>
            <script src="{% static 'js/jquery_v4.0.0.js' %}"></script>
            <script src="{% static 'js/datatables.js' %}"></script>
            {% block script %}{% endblock %}
          </head>
        </html>
        ```

10. ## Manejo de Base de Datos
    Una base de datos en entornos profesionales debe controlarse con usuarios específicos con permisos otorgados explícitamente. Esto lo lograremos ejecutando sentencias SQL directamente en el motor de DB, de la siguiente forma:
    - Crear usuario remoto 'Usuario' con contraseña 'mi_contraseña'

      ```
      CREATE USER 'Usuario'@'%' IDENTIFIED BY 'mi_contraseña';
      ```

    - Conceder privilegios para una base de datos específica al usuario remoto 'Usuario' (por ejemplo, 'mi_base_datos')

      ```
      GRANT ALL PRIVILEGES ON mi_base_datos.* TO 'Usuario'@'%';
      ```

    - Aplicar los cambios de privilegios (permisos)

      ```
      FLUSH PRIVILEGES;
      ```

    - ORM: Para comunicarnos con la DB usaremos un ORM (_Object Relational Mapping_), que se encargará de entender los objetos (por el lado del código) y las entidades (por el lado de la base de datos).

      | Código |          | Base de datos |
      | ------ | -------- | ------------- |
      | Clase  | <------> | Entidad       |
      | objeto | <------> | registro      |

    - Usaremos _SqlAlchemy_ como _ORM_, junto con el driver de base de datos _mysqlclient_, los que se instalarán mediante la ejecución del siguiente comando en el terminal:

      ```
      pip install SQLAlchemy mysqlclient
      ```

    - Una vez con la base de datos creada, procedemos a modificar nuestro archivo settings.py. Indicamos que haremos uso del gestor MySQL, en vez de SQLite que usa por defecto Django, modificando la sección _DATABASES_ del archivo _motor_django/settings.py_:

      ```
      DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.mysql',
              'NAME': 'mi_db',
              'USER': 'mi_usuario',
              'PASSWORD': 'mi_password',
              'HOST': 'localhost',
              'PORT': '3306'
          }
      }
      ```

11. ## Modelo de Datos
    - Django controlará la base de datos mediante migraciones, scripts de bases de datos que modificarán la estructura de datos.
    - Django maneja varias tablas de manera predeterminada para información interna, para que se creen en la DB, debemos ejecutar el comando:

      ```
      python manage.py migrate
      ```

    - Este comando aplicó una serie de migraciones nativas de Django en la base de datos, como permisos, usuarios, autorizaciones, sesiones, etc...
    - El siguiente paso es aplicar NUESTRO modelo a la base de datos. Para crear los modelos debemos modificar el archivo _mi_aplicacion/models.py_ y agregar las _clases_ que hemos determinado para nuestro proyecto. Idealmente debiéramos tener un diagrama entidad-relación o uno de clases para tener claro el modelo de datos.
    - Nuestras clases se crearán heredando desde _models_ de Django, para poder acceder a los ditintos tipos de datos que deberá tener como atributos.
    - Estructura de creación de nuestro modelo:

      ```
      from django.db import models

      class MiClase(models.Model):
          atributo_1 = models.CharField('Campo 1',max_length=25,null=false)
          atributo_2 = models.TextField('Campo 2',max_length=100,null=false)
          atributo_3 = models.DateField('Campo 3',null=false)
          atributo_4 = models.TimeField('Campo 4',null=false)
          atributo_5 = models.DateTimeField('Campo 5',max_length=100,null=false)
          atributo_6 = models.IntegerField('Campo 6',)
          atributo_7 = models.DecimalField('Campo 7',)
          atributo_8 = models.FloatField('Campo 8',)
          atributo_9 = models.EmailField('Campo 9',)
          atributo_10 = models.BooleanField('Campo 10',default=true)
          atributo_11 = models.URLField('Campo 11',default=true)
          created_at = models.DateTimeField('Fecha Creación',default=ahora)
          updated_at = models.DateTimeField('Fecha Actualización',auto_now=True)

      class MiClase2(models.Model):
          atributo_referenciado = models.ForeignKey(MiClase,on_delete=CASCADE)
          atributo_2 = models.CharField(max_length=100)
          created_at = models.DateTimeField(default=ahora)
          updated_at = models.DateTimeField(auto_now=True)
      ```

    - Cada tipo de dato heredado desde _models_ tiene algunos argumentos, los que pueden ser comunes, aplicacbles a cualquier tipo de dato, o específicos, que dependen del tipo de campo:
      Argumentos comunes:
      - null=True / False: Si es True, Django almacenará los valores vacíos como NULL en la base de datos. Por defecto es False.
      - blank=True / False: Si es True, el campo puede quedar vacío en los formularios de validación. Por defecto es False.
      - default: Define un valor por defecto para el campo si no se proporciona ninguno. Puede ser un valor estático o una función ejecutable (como timezone.now).
      - choices: Una secuencia (lista o diccionario) de opciones para crear un menú desplegable en los formularios.
      - unique=True / False: Si es True, asegura que el valor de este campo sea único en toda la tabla de la base de datos.
      - verbose_name: Un nombre interactivo y legible para humanos que describe el campo. Si no se declara, Django lo genera automáticamente usando los guiones bajos del nombre de la variable.
      - primary_key=True / False: Si es True, establece explícitamente este campo como la clave primaria del modelo.
      - help_text: Un texto de ayuda adicional que se muestra junto al campo en los formularios del administrador.
      - editable=True / False: Si es False, el campo no se mostrará en el panel de administración ni en otros formularios.

      Argumentos Espefíficos:
      - Para cadenas de texto (CharField, SlugField, etc.)
        -max_length: Obligatorio para CharField. Define la cantidad máxima de caracteres permitidos en la base de datos.
      - Para números decimales (DecimalField)
        - max_digits: Obligatorio. El número máximo de dígitos permitidos en total (incluyendo decimales).
        - decimal_places: Obligatorio. El número de posiciones decimales a almacenar.
      - Para fechas y tiempo (DateTimeField, DateField)
        - auto_now=True: Actualiza automáticamente el campo con la fecha/hora actual cada vez que el objeto se guarda (útil para campos como updated_at).
        - auto_now_add=True: Guarda automáticamente la fecha/hora actual solo cuando el objeto se crea por primera vez (útil para created_at).

      Argumentos para Relaciones (ForeignKey, OneToOneField, ManyToManyField)
      - to: Obligatorio. El modelo con el que se relaciona (puede pasarse como la clase directamente o como un string 'App.Modelo').
      - on_delete: Obligatorio. Define qué sucede con este registro si el objeto relacionado se elimina. Los más comunes son:
        - models.CASCADE: Borra también este registro.
        - models.SET_NULL: Pone el campo en NULL (requiere null=True).
        - models.PROTECT: Evita la eliminación del objeto relacionado.
      - related_name: El nombre que se utilizará para la relación inversa desde el modelo relacionado hacia este

    - Con nuestras clases ya creadas, debemos GENERAR una nueva migracion con el comando:

      ```
      python manage.py makemigrations
      ```

    - Una vez que se ha creado nuestra nueva migración, debemos aplicarla a la base de datos, ejecutando nuevamente el comando:

      ```
      python manage.py migrate
      ```

    > Cada vez que modifiquemos el modelo de datos, crearemos una nueva migración y la aplicaremos a la base de datos para que se actualice de acuerdo a nuestro modelo.

12. ## Datos Iniciales de la Aplicación
    Al estar definida nuestra base de datos y aplicadas las migraciones de nuestro modelo de datos, tenemos la estructura de datos requerida para alojar nuestros registros.
    En este punto será importante contar con datos genéricos iniciales de la aplicación, como listas o parámetros que deben estar pre-cargados.
    Esto lo lograremos de la siguiente forma:
    - Dentro del directorio de nuestra aplicación crearemos un nuevo directorio _fixtures_ que es donde guardaremos los archivos con datos en formato _JSON_ para que sean cargados en la DB.
    - Para cada dato requerido generaremos un archivo _.json_ que contendrá los datos necesarios.
    - La estructura de este archivo dependerá de nuestro modelo, pero siguiendo el siguiente patrón:

      ```
      [
          {
              "model": "mi_aplicacion.nombre_modelo",
              "pk": 1,
              "fields": {
                  "atributo_1": "01",
                  "atributo_2": "Atributo 2"
              }
          },
          {
              "model": "mi_aplicacion.nombre_modelo",
              "pk": 2,
              "fields": {
                  "atributo_1": "02",
                  "atributo_2": "Atributo 2"
              }
          }
      ]
      ```

    Donde _"pk"_ es el campo _id_ generado de manera automática por Django y _fields_ serán los atributos de nuestro modelo.

13. ## Desacoplar Datos Sensibles
    Ahora que ya estamos trabajando con una DB externa, debemos usar credenciales para conectarnos a esta nueva DB. Cualquier credencial o dato sensible no debería existir en código, incluyendo la _'SECRET_KEY'_ de Django, por lo que debemos _DESACOPLAR_ esos datos y ponerlos en un archivo de ambiente.
    - Instalamos la librería _decouple_ para desacoplar los datos y posteriormente leerlos desde un archivo de ambiente. El siguiente comando será necesario para instalar la librería:

      ```
      pip install python-decouple
      ```

    - Creamos un archivo _.env_ (archivo de ambiente, env de environment) en el directorio principal de la aplicación o donde se encuentre su archivo _manage.py_.
    - En el archivo _.env_ ponemos los datos sensibles en variables que tendrán como valor el dato. Es importante no dejar espacios entre el nombre de la variable y la asignación del valor:

      ```
      SECRET_KEY='cadena_de_caracteres_django_secret_key'
      ```

    - Donde necesitemos usar ese dato, generalmente en _setting.py_, importaremos el método _config_ de la librería _decouple_ para acceder a los datos almacenados en el archivo de ambiente, de la siguiente forma:
      _settings.py_

      ```
      from decouple import config

      SECRET_KEY = config('SECRET_KEY')
      ```

    El método _config_ traerá el valor de la variable almacenada en el archivo de ambiente que tenga el nombre que le pasamos al método como argumento.
    El mismo procedimiento debemos usar para procesar la información de la base de datos.

14. ## Instalación Django Rest Framework
    Django Rest Framework es una librería que contiene muchas herramientas que usaremos en nuestro desarrollo django, como los serializadores.
    Para instalarlo ejecutaremos el siguiente comando mediante terminal:

        pip install djangorestframework

    Una vez que se ha instalado, debemos agregarlo a la lista de _INSTALLED_APPS_ en _settings.py_ de nuestro motor Django.

        INSTALLED_APPS = [
            ...
            'rest_framework',
            ...
        ]

15. ## Incorporar Modelo de Datos al administrador de Django
    En el archivo _mi_aplicacion/admin.py_ debemos _REGISTRAR_ nuestro modelo de datos, para que el admin de django pueda procesar los datos.
    Esto lo lograremos de la siguiente forma:
    _admin.py_

        from django.contrib import admin
        from .models import MiClase
        from .models import MiClase2

        # Register your models here.
        admin.site.register(MiClase)
        admin.site.register(MiClase2)

    Cuando ingresemos a la aplicación, en la sección _admin_ podremos hacer _CRUD_ de cada objeto de nuestro modelo de datos que haya sido registrado.

16. ## Creación de Serializadores
    La librería _rest_framework_ que instalamos anteriormente, tiene la herramienta para serializar nuestro modelo de datos en formato _JSON_, que será necesario para trabajar los datos en la aplicación web, lo que lograremos siguiendo estos pasos:
    - Primero crearemos un archivo _serializer.py_ en el directorio de nuestra aplicación.
    - En el archivo creado, importaremos _serializers_ para usarlos en la serialización de nuestro modelo.
    - Junto con esto, debemos importar todo nuestro modelo de datos desde _models.py_.
    - Finalmente, crearemos una clase que se encargará de serializar cada uno de nuestros modelos de datos.

    El archivo debiera quedar como el siguiente ejemplo:

        from rest_framework import serializers

        from . import models

        class MiClaseSerializer(serializers.ModelSerializer):
            class Meta:
                model = models.MiClase
                fields = ('__all__')
                # __all__ serializa todas los atributos de la clase/modelo

        class MiClase2Serializer(serializers.ModelSerializer):
            class Meta:
                model = models.MiClase2
                fields = ('atributo_referenciado','atributo_2')
                # De esta forma nosotros decidimos qué atributos de nuestra clase/modelo se serializarán

17. **Creación de Vistas CBV**
    CBV es el acrónimo de Class Based View o _Vista Basada en Clase_, es una colección de vistas basadas en un modelo de datos y que nos permiten hacer _CRUD_ de los datos de ese modelo.
    Las vistas basadas en clase se crearán dentro de _mi_aplicacion/views.py_, nuestro archivo controlador, siguiendo las siguientes instrucciones:
    - Importamos todos nuestros modelos de datos al archivo _views.py_.
    - Junto con la importación de las clases, importamos nuestros serializadores, puesto que se ancargarán de dejar los datos en un formato que podamos usar en las vistas.
    - con todo esto ya podemos crear nuestro _ViewSet_, o colección de vistas para trabajar con los datos del modelo desde Django.

    El archivo debería quedar de la siguiente forma:

    ```
    from rest_framework import viewsets
    from . import models
    from . import serializer

    class MiClaseViewSet(viewsets.ModelViewSet):
        queryset = models.MiClase.objects.all()
        serializer_class = serializer.MiClaseSerializer

    class MiClase2ViewSet(viewsets.ModelViewSet):
        queryset = models.MiClase2.objects.all()
        serializer_class = serializer.MiClase2Serializer
    ```

18. **Creación de Rutas**
    Los ViewSet que creamos en el paso anterior generan las vistas y métodos para hacer el _CRUD_ de nuestros datos con métodos _HTTP/S_ de tipo _POST_, _GET_, _PUT/PATCH_ o _DELETE_, pero ahora necesitamos llegar hasta esos métodos o _END-POINTS_, por lo que debemos generar las rutas necesarias.
    - En el directorio de nuestra aplicación creamos un nuevo archivo _urls.py_, donde gestionaremos todas las rutas necesarias para nuestro modelo de datos completo.
    - Dentro de este archivo, generaremos un objeto _enrutador_ (routers.DefaultRouter) que se encargará de generar las rutas para los métodos mencionados.
    - Para crear las rutas usaremos el método _register_ disponible dentro del objeto enrutador. Este método recibe como primer argumento el nombre que le daremos al conjunto de rutas de un _ViewSet_ y como segundo argumento le indicaremos cuál será el ViewSet que registraremos, por lo que el archivo quedará de la siguiente forma:

      ```
      from django.urls import path,include
      from rest_framework import routers
      from mi_aplicacion import views

      enrutador = routers.DefaultRouter()

      enrutador.register(r'miclase', views.MiClaseViewSet)
      enrutador.register(r'miclase2', views.MiClase2ViewSet)

      urlpatterns = [
          path('', include(enrutador.urls))
      ]
      ```

    - La _r_ delante del string para generar la ruta es para evitar saltos de línea generados cuando se crea la ruta, es un tipo de dato _RAW_ de Python.
    - El _urlpatterns_ incluirá todas las rutas generadas dentro del enrutador y será necesario para enviarlas a _motor_django/urls.py_.

19. **Incorporación de rutas a Django**
    - Para que las rutas generadas en la aplicación queden disponibles dentro de _django/urls.py_, debemos importarlas e incluirlas, de la siguiente forma:

      ```
      from django.contrib import admin
      from django.urls import path,include
      from mi_aplicacion import views

      urlpatterns = [
          path('admin/', admin.site.urls),
          path('', views.inicio),
          path('mi_aplicacion/', include('mi_aplicacion.urls')),
      ]
      ```

    - Con todo lo anterior, ya podemos iniciar nuestra aplicación, dirigirnos a: *http://127.0.0.1:8000/mi_aplicacion/* y comenzar a hacer _CRUD_ de nuestros modelos.

20. **CRUD Manual**

    En los pasos anteriores usamos _ViewSet_ de Django REST Framework para exponer un CRUD mediante una API. Esta herramienta que Django disponibiliza no es la que debe usar un usuario de aplicación, porque puede que no tenga los conocimientos técnicos necesarios y evita validaciones que no estén incluidas en el modelo de datos, por lo que se hace necesario generar una aplicación completamente funcional para hacer toda la gestión de nuestros datos.
    En este apartado construiremos las vistas tradicionales de Django para listar, crear, editar y consultar registros desde plantillas HTML. También agregaremos la opción de habilitar o deshabilitar un registro sin eliminarlo de la base de datos, lo que conocemos como eliminado lógico.

    ### Crear los formularios

    Crea el archivo _mi_aplicacion/forms.py_. Usaremos un _ModelForm_ para que Django genere el formulario de creación y edición a partir de los campos del modelo. En el siguiente ejercicio deberás reemplazar los campos del ejemplo por los que existan en tu modelo. Una consideración especial tendremos con el campo _habilitado_, el que se gestiona por separado para evitar que se cambie desde el formulario de edición:

    ```
    from django import forms
    from .models import MiModelo

    class MiModeloForm(forms.ModelForm):
      class Meta:
        model = MiModelo
        fields = ['nombre', 'descripcion']
        widgets = {
          'nombre': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre del registro...'
          }),
          'descripcion': forms.Textarea(attrs={
            'class': 'form-control',
              'rows': 4
            })
          }

        class CambiarEstadoForm(forms.ModelForm):
          class Meta:
            model = MiModelo
            fields = ['habilitado']
    ```

    Los _widgets_ permiten definir cómo se representa cada campo en HTML y agregar clases CSS, por ejemplo, las clases de Bootstrap.
    El campo _habilitado_ será usado por un método que crearemos más adelante, _CambiarEstadoForm_, para deshabilitar o habilitar el objeto en cuestión.

    ### Crear las vistas

    En _mi_aplicacion/views.py_ importa las vistas genéricas, los formularios y el modelo. Luego, crea las vistas en el siguiente orden:
    1.  **ListView**

        _ListView_ obtiene los registros del modelo indicado en _model_ y los entrega a una plantilla indicada mediante _template_name_. Por defecto, la lista de los objetos obtenidos desde la base de datos queda disponible en el elemento _object_list_, que queda dentro de la plantilla:

            from django.views.generic import ListView
            from .models import MiModelo

            class RegistroListView(ListView):
                model = MiModelo
                template_name = 'mi_aplicacion/registros/lista_registros.html'

    2.  **CreateView**

        _CreateView_ muestra y procesa el formulario de creación, _form_class_, en la vista _template_name_, de acuerdo al modelo indicado en _model_. Al guardarlo correctamente, redirige a la URL incluida en _success_url_:

             from django.urls import reverse_lazy
             from django.views.generic import CreateView
             from .forms import MiModeloForm

             class RegistroCreateView(CreateView):
                 model = MiModelo
                 form_class = MiModeloForm
                 template_name = 'mi_aplicacion/registros/crear_registro.html'
                 success_url = reverse_lazy('listado_registros')

    3.  **UpdateView**

        _UpdateView_ localiza el registro mediante el parámetro _pk_ de la ruta, carga sus valores actuales en el formulario y guarda los cambios.
        Puede incluso usar el mismo form incluído en la vista de creación.
        Para redirigir a una URL específica, debemos incluirla dentro del método _reverse_lazy_, porque el código de la clase se carga antes que el mapa de URL's. Con esta instrucción hacemos que el objeto espere hasta que sea actualizado y ya esté cargado el mapa de URL's:

            from django.views.generic import UpdateView

            class RegistroUpdateView(UpdateView):
                model = MiModelo
                form_class = MiModeloForm
                template_name = 'mi_aplicacion/registros/editar_registro.html'
                success_url = reverse_lazy('listado_registros')

    4.  **Método para deshabilitar o habilitar**

        Antes de crear esta vista, agrega a la clase de tu modelo en _mi_aplicacion/models.py_ un campo booleano. Así el registro se podrá deshabilitar sin eliminarlo de la base de datos:

            habilitado = models.BooleanField(default=True)

        Si el modelo ya tiene migraciones aplicadas, crea y aplica una migración desde el terminal con el ambiente virtual activado:

            .\mi_ambiente\Scripts\Activate
            python manage.py makemigrations
            python manage.py migrate

        Asegúrate de que _CambiarEstadoForm_ en _mi_aplicacion/forms.py_ incluya el campo _habilitado_. Luego crea la vista con _UpdateView_; el método _form_valid_ guarda el cambio y redirige al listado:

            from django.shortcuts import redirect
            from django.views.generic import UpdateView
            from .forms import CambiarEstadoForm

            class CambiarEstadoView(UpdateView):
                model = MiModelo
                form_class = CambiarEstadoForm

                def form_valid(self, form):
                    self.object = form.save()
                    return redirect('listado_registros')

        La vista también permite habilitar nuevamente un registro enviando _habilitado=True_.

    5.  **DetailView (opcional)**

        Para consultar los datos de un registro individual, agrega _DetailView_. También busca el objeto mediante el parámetro _pk_:

            from django.views.generic import DetailView

            class RegistroDetailView(DetailView):
                model = MiModelo
                template_name = 'mi_aplicacion/registros/detalle_registro.html'

        El objeto queda disponible en la plantilla como un objeto al que podemos acceder de la manera habitual en Django y mostrarlo de la forma que mas nos convenga, por ejemplo dentro de un elemento _CARD_ de Bootstrap.

        ```
        <div class="card border-dark mb-3">
            <div class="card-header">{{ mimodelo.nombre }}</div>
            <div class="card-body">
                <h4 class="card-title">{{ mimodelo.id }}</h4>
                <p class="card-text">{% if mimodelo.descripcion is not None %}{{ mimodelo.sinopsis }}{% else %}--{% endif %}</p>

                <div class="col">
                    <a href="{% url 'actualizar_mimodelo' mimodelo.id %}" class="btn btn-success" title="Editar {{mimodelo.nombre}}"><i class="bi bi-pencil-fill"></i></a>
                </div>
            </div>
        </div>
        ```

    ### Crear las rutas

    En _mi_aplicacion/urls.py_ agrega una ruta para cada vista. Las rutas de edición, detalle y cambio de estado reciben el identificador del registro:

        from django.urls import path
        from . import views

        urlpatterns = [
            path('mimodelo/', views.MiModeloListView.as_view(), name='listado_mimodelo'),
            path('mimodelo/crear/', views.MiModeloCreateView.as_view(), name='crear_mimodelo'),
            path('mimodelo/<int:pk>/editar/', views.MiModeloUpdateView.as_view(), name='editar_mimodelo'),
            path('mimodelo/<int:pk>/detalle/', views.MiModeloDetailView.as_view(), name='detalle_registro'),
            path('mimodelo/<int:pk>/cambiar_estado/', views.CambiarEstadoView.as_view(), name='cambiar_estado'),
        ]

    Verifica que _mi_aplicacion/urls.py_ esté incluido en _motor_django/urls.py_, tal como se explicó en [Incorporación de rutas a Django](#).

    ### Crear las plantillas

    Crea el directorio _mi_aplicacion/templates/mi_aplicacion/registros/_ y dentro de él las plantillas indicadas en _template_name_. En la plantilla _lista_registros.html_, _ListView_ entrega los elementos mediante _object_list_:

        <h3>Listado de registros</h3>
        <a href="{% url 'crear_registro' %}">Agregar registro</a>

        <table>
            <thead>
                <tr><th>Nombre</th><th>Estado</th><th>Acciones</th></tr>
            </thead>
            <tbody>
                {% for registro in object_list %}
                <tr>
                    <td>{{ registro.nombre }}</td>
                    <td>{% if registro.habilitado %}Habilitado{% else %}Deshabilitado{% endif %}</td>
                    <td>
                        <a href="{% url 'editar_registro' registro.pk %}">Editar</a>
                        <a href="{% url 'detalle_registro' registro.pk %}">Ver detalle</a>
                        {% if registro.habilitado %}
                        <button type="button" class="cambiar-estado"
                            data-url="{% url 'cambiar_estado' registro.pk %}"
                            data-current="true">Deshabilitar</button>
                        {% else %}
                        <button type="button" class="cambiar-estado"
                            data-url="{% url 'cambiar_estado' registro.pk %}"
                            data-current="false">Habilitar</button>
                        {% endif %}
                    </td>
                </tr>
                {% empty %}
                <tr><td colspan="3">No se encontraron registros.</td></tr>
                {% endfor %}
            </tbody>
        </table>
        {% csrf_token %}

        <script>
            document.addEventListener('click', function (event) {
                const button = event.target.closest('.cambiar-estado');
                if (!button) return;

                const nextState = button.dataset.current !== 'true';
                const formData = new FormData();
                formData.append('habilitado', nextState);

                const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
                fetch(button.dataset.url, {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': csrfToken,
                        'X-Requested-With': 'XMLHttpRequest'
                    },
                    body: formData
                })
                    .then(response => {
                        if (response.ok) {
                            window.location.reload();
                        } else {
                            alert('No fue posible cambiar el estado del registro.');
                        }
                    })
                    .catch(error => console.error('Error al cambiar el estado:', error));
            });
        </script>

    El botón envía el estado contrario al actual mediante _fetch_ y una solicitud _POST_. _{% csrf_token %}_ genera el token que Django valida en el encabezado _X-CSRFToken_. Al guardar, _CambiarEstadoView_ actualiza el campo _habilitado_ y la página se recarga para mostrar el nuevo estado. Así, el registro permanece en la base de datos y puede habilitarse nuevamente.

    Para las plantillas _crear_registro.html_ y _editar_registro.html_, puedes reutilizar un formulario HTML como el siguiente. Django muestra los campos del _ModelForm_; en la edición, _UpdateView_ los completa con los valores actuales:

        <form method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <button type="submit">Guardar</button>
        </form>

    En _detalle_registro.html_ puedes mostrar los datos recibidos en la variable _registro_, definida en _context_object_name_ de _RegistroDetailView_:

        <h3>{{ registro.nombre }}</h3>
        <p>{{ registro.descripcion }}</p>
        <p>{% if registro.habilitado %}Habilitado{% else %}Deshabilitado{% endif %}</p>

    Puedes reemplazar el HTML sencillo de estos ejemplos por tus componentes y estilos, manteniendo las rutas, los nombres de los formularios y los campos correspondientes a tu modelo.

21. **Inicio de Sesión con Django**
    El sistema de autenticación incluido con Django se centra en el modelo User, lo que permite manejar cuentas de usuario, permisos, y tareas esenciales como login, logout, y control de contraseñas.

    Django provee vistas de autenticación y herramientas para todo lo relacionado.
    - Django proporciona URLs de autenticación listas para usar. Añádelas en el archivo urls.py de tu proyecto Django:

      ```
      from django.urls import include, path
      from django.contrib.auth import views as auth_views

      urlpatterns = [
          path('admin/', admin.site.urls),
          # …

          # URL's de autenticación
          path('accounts/', include('django.contrib.auth.urls')),
          path('login/', auth_views.LoginView.as_view(), name='login'),
          path('logout/', auth_views.LogoutView.as_view(), name='logout'),
          path('registro/', views.registro, name='registro')
      ]
      ```

    - Django busca plantillas de autenticación en un directorio llamado registration. Crea la carpeta dentro de mi_aplicacion/templates y añade la plantilla login.html:

      ```html
      {% extends "plantilla_base.html" %}
      <title>{% block titulo %}Login{% endblock%}</title>
      {% block content %}
      <form method="post" action="{% url 'login' %}">
        {% csrf_token %}

        <div>
          <label for="username">Nombre Usuario:</label>
          <input type="text" id="username" name="username" required />
        </div>
        <div>
          <label for="password">Contraseña:</label>
          <input type="password" id="password" name="password" required />
        </div>
        {% if form.errors %}
        <p>
          Tu nombre de usuario y contraseña no coinciden. Inténtalo nuevamente.
        </p>

        <div class="error">{{ form.non_field_errors }}</div>

        {% endif %}
        <button type="submit">Login</button>
      </form>
      <p><a href="{% url 'password_reset' %}">¿Olvidaste tu contraseña?</a></p>
      {% endblock %}
      ```

    - Añade la siguiente configuración en tu archivo _settings.py_ para redirigir a los usuarios a la página de inicio después de iniciar sesión:

      ```
      LOGIN_REDIRECT_URL = '/'
      ```

    - Luego debemos agregar usuarios y grupos, lo que puede hacerse mediante django admin.
    - Para restringir el acceso a FBV debemos usar decoradores:

      ```
      from django.contrib.auth.decorators import login_required

      @login_required
      def mi_vista(request):
      ```

    - Para restringir el acceso a CBV, usaremos la validación por defecto de DRF, con el siguiente decorador:

      ```
      from rest_framework.authentication import
      SessionAuthentication

      class MiClaseViewSet(viewsets.ModelViewSet):
          authentication_classes = [SessionAuthentication]
          # Otras configuraciones de la vista...
      ```

    - Para que el usuario pueda salir de la sesión, simplemente agregamos un botón para salir directamente en la plantilla base:

      ```html
      {% if request.user.is_authenticated %}
      <form
        id="logout-form"
        action="{% url 'logout' %}"
        method="post"
        style="display: inline;"
      >
        {% csrf_token %}
        <button type="submit">Cerrar sesión</button>
      </form>
      {% else %}
      <a href="{% url 'login' %}">Iniciar sesión</a>
      {% endif %}
      ```

    - Creamos la vista de registro directamente como FBV en _views.py_:

      ```
      from django.contrib import messages
      from django.contrib.auth.forms import UserCreationForm

      def registro(request):
          if request.method == 'POST':
              form = UserCreationForm(request.POST)
              if form.is_valid():
                  user = form.save()
                  login(request, user)
                  messages.success(request, "Registro Exitoso. ¡Bienvenido!")
                  return redirect('/')
              else:
                  messages.error(request, "No ha sido posible Registrarlo. Por favor revise el formulario por errores.")
          else:
              form = UserCreationForm()
          return render(request, 'registro.html', {'form':form})
      ```

    - Ahora que definimos la vista, creamos el formulario.
    - Dentro de la carpeta registration, creamos un archivo registro.html, que tendrá un formulario muy simple, pero que es renderizado desde UserCreationForm, como lo indicamos en views.py. En este archivo incluiremos lo siguiente:

      ```html
      {% block content %}
      <form method="post">
        {% csrf_token %} {{ form.as_p }} {% if form.errors %}
        <p>Registro incorrecto. Inténtelo nuevamente.</p>

        {% endif %}
        <button type="submit">Register</button>
      </form>
      {% endblock %}
      ```

    - Finalmente, podremos acceder, almacenar y modificar la información de sesión en las vistas, usando request.session:

      ```
      @login_required
      def pagina_inicio(request):
          # Almacenar data en SESSION
          request.session['mensaje_bienvenida'] = '¡Bienvenido!'

          # Obtener data desde SESSION
          mensaje_bienvenida = request.session.get('mensaje_bienvenida')

          # Remover data desde SESSION
          if 'mensaje_bienvenida' in request.session:
              del request.session['mensaje_bienvenida']

          return render(request, 'mi_aplicacion/inicio.html', {'message': mensaje_bienvenida})
      ```

    - Podemos controlar el comportamiento de la sesión al modificar settings.py:

      ```
      # SESSION expira después de 1 hora
      SESSION_COOKIE_AGE = 3600

      # SESSION expira al cerrar el navegador
      SESSION_EXPIRE_AT_BROWSER_CLOSE = True

      # Usamos la DB para SESSION
      SESSION_ENGINE = 'django.contrib.sessions.backends.db'
      ```

    - Para verificar el estado de la sesión en nuestras vistas, modificamos el archivo views.py:

      ```
      from django.shortcuts import redirect

      def vista_protegida(request):
          if not request.user.is_authenticated:
              # Redirecciona a login si el usuario no está autenticado
              return redirect('login')
          return render(request, 'vista_protegida.html')
      ```

    - Para cerrar una sesión de usuario y limpiar la data de sesión, usamos la vista FBV logout:

      ```
      def logout_view(request):
          # Cierra la sesión del usuario y limpia la data de SESSION
          logout(request)
          # Redirige a la página de inicio de sesión
          return redirect('login')
      ```

    ### Extensión de User

    Podemos crear nuestro propio modelo de usuario, pero si usamos el nativo podemos mantener todo el sistema de autenticación (como el inicio de sesión con login(), contraseñas, permisos) y, al mismo tiempo, agregar nuestros propios campos personalizados. La mejor práctica para lograrlo es extender el modelo de usuario utilizando AbstractUser, de la siguiente forma:
    - Debemos definir el modelo personalizado en el archivo _mi_aplicacion/models.py_, y heredar de AbstractUser:

      ```
      from django.contrib.auth.models import AbstractUser
      from django.db import models

      class MiUsuario(AbstractUser):
          # Agrega tus propios campos aquí
          telefono = models.CharField(max_length=20, blank=True, null=True)
          fecha_nacimiento = models.DateField(blank=True, null=True)
          biografia = models.TextField(blank=True)

          def __str__(self):
              return self.username
      ```

    - Debes indicarle a Django que use tu nuevo modelo en lugar del modelo por defecto. Añade la siguiente línea en tu archivo _motor_django/settings.py_:

      ```
      AUTH_USER_MODEL = 'mi_aplicacion.MiUsuario'
      ```

    - Para que puedas gestionar tus usuarios personalizados y ver tus nuevos campos desde el panel de administración de Django, usa _UserAdmin_ para registrar tu modelo en _mi_aplicacion/admin.py_:

      ```
      from django.contrib import admin
      from django.contrib.auth.admin import UserAdmin
      from .models import MiUsuario

      # Esto asegura que los campos heredados y los nuevos se muestren correctamente
      admin.site.register(MiUsuario, UserAdmin)
      ```

---

## Crear un Usuario Admin de Django

El usuario _ADMIN_ de Django es el que tendrá control administrativo de la aplicación y también podrá hacer _CRUD_ de nuestro modelo de datos.
Para crearlo, ejecutaremos el siguiente comando mediante nuestro terminal:

```
python manage.py createsuperuser
```

Una vez que jecutamos el comando, este nos pedirá la información del usuario mediante el mismo terminal.

---

## Control de Dependecias

Para poder mantener las librerias actualizadas y estandarizadas para todo el equipo de desarrollo, crearemos un archivo de requerimientos con el siguiente comando:

    ```
    pip freeze > requirements.txt
    ```

Este archivo tendrá una lista de todas las librerías incluídas en nuestro _VENV_, las que posteriormente podrán ser instaladas en cualquier nuevo _VENV_ ejecutando el siguiente comando:

    ```
    pip install -r requirements.txt
    ```

> Cada vez que agreguemos una nueva librería actualizaremos el archivo de requerimientos con el comando _FREEZE_.

---

## Control de Fechas Global

Si se necesita aplicar el mismo formato de fecha en toda la aplicación, debemos agregar un configuración global en _settings.py_ como un diccionario llamado _REST_FRAMEWORK_.

    ```
    REST_FRAMEWORK = {
        'DATETIME_FORMAT': '%Y-%m-%d %H:%M:%S',

        # Formatos de entrada global aceptados por campos DateTimeFields
        'DATETIME_INPUT_FORMATS': ['%d-%m-%Y %H:%M:%S', '%d-%m-%Y', 'iso-8601'],

        # Formato de salida global para campos DateFields
        'DATE_FORMAT': '%d-%m-%Y',

        # Formatos de entrada global aceptados por campos DateFields
        'DATE_INPUT_FORMATS': ['%d-%m-%Y'],
    }
    ```

---