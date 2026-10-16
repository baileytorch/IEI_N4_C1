# IEI_N4_C1
Clases de Backend con Django

Como buenos desarrolladores, ya debemos tener creado un repositorio para trabajar el código de la aplicación que debemos construir.
- Si no ha trabajado aún con repositorios, he construido una pequeña guía paso a paso que está disponible en sus ambientes de aprendizaje.
- Cada estudiante debe construir un proyecto que se ha asignado con anterioridad. La lista de estudiantes con los proyectos asignados y la descripción de los proyectos, los puede encontrar en su ambiente de aprendizaje.

## Creación de Proyectos con Django

1. **Creación de Ambiente Virtual**
    - Habiendo creado y clonado nuestro repositorio, abrimos la carpeta contenedora en VS Code.
    - Dentro de este directorio, crearemos un ambiente virtual que mantendrá aislada toda la configuración de nuestro proyecto y su entorno de trabajo.
    - Para lograrlo, iniciaremos un nuevo terminal, estando ubicados en el directorio principal.
    - Para crear el ambiente virtual, ejecutamos el siguiente comando en el terminal:
        ```
        python -m venv nombre_ambiente
        ```

    - *VENV* es acrónimo de *VIRTUAL ENVIRONMENT*, por lo que debemos entender que creará nuestro ambiente virtual.
    - *nombre_ambiente* debe ser reemplazado por el nombre que Ud. le quiera dar a su ambiente virtual. Es recomendable que sea corto y descriptivo.
    - Nuestro nuevo ambiente virtual tiene 2 directorios muy importantes:
        - *Libs*: Directorio donde encontraremos las librerías asociadas a nuestro proyecto. Cuando está recién creado, sólo contendrá *PIP*.
        - *Scripts*: Directorio que contiene distintos scripts que serán usados durante el desarrollo, como Activate y deactivate.
    
2. **Activación de Ambiente Virtual**
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

    - Habiendo ejecutado este comando, ya deberíamos poder ejecutar el comando *Activate* y activar nuestro ambiente virtual.
    - Si hemos terminado de trabajar, o debemos cambiarnos de proyecto, necesitamos desactivar el ambiente virtual, para lo que usaremos el siguiente comando:
        ```
        deactivate
        ```

    - Todo lo que haremos a continuación debe ser fuera de este directorio, por lo que debemos salir hasta el directorio principal mediante el siguiente comando:
        ```
        cd..
        ```

    - El comando *cd..* permite salir de un directorio y ubicarnos en el superior, por lo que deberíamos ejecutarlo 2 veces para llegar al directorio principal, saliendo de *mi_ambiente\Scripts*.

3. **Actualización de PIP**
    - A pesar de haber generado una instalación del entorno desde cero, no está asegurado que contenga la última versión de PIP, por lo que debemos actualizarlo.
    - Para lograrlo, ejecutamos el siguiente comando en nuestro terminal:
        ```
        python -m pip install --upgrade pip
        ```

4. **Instalación de Entorno Django**
    - Mediante terminal, estando ubicados en el directorio raíz de la aplicación, ejecutaremos el siguiente comando:
        ```
        pip install django
        ```

    - El comando anterior instaló todas las dependencias necesarias para que Django pueda trabajar, las que deberían haber quedado en *mi_ambiente\Libs*. Estas debieran ser:
        - asgiref.
        - django.
        - sqlparse.
        - tzdata.
    - Ahora crearemos el entorno de trabajo de Django mediante el comando:
        ```
        django-admin startproject motor_django .
        ```

    - No debe olvidar el *PUNTO* al final del comando, para indicar que el directorio de Django se debe crear en el directorio principal de trabajo.
    - Este comando creó la estructura de archivos de Django con nombre *motor_django*, el que Ud. puede cambiar al que guste. Debemos recordar que debe ser suficientemente descriptivo, por lo que es común usar el acrónimo *drf* por *Django Rest Framework*.
    - Este directorio contiene los archivos de configuración de Django, dentro de los que tenemos. 
        - *settings.py*, contiene configuraciones generales, como la conexión a la base de datos.
        - *urls.py*, contiene las rutas para redirigir las solicitudes *REQUEST* que lleguen a la aplicación.

5. **Creación de la Aplicación**
    - A continuación, para crear la aplicación que debemos construir, ejecutaremos el siguiente comando mediante terminal:
        ```
        django-admin startapp mi_aplicacion
        ```

    - El comando anterior creó un nuevo directorio llamado *mi_aplicacion*, igual que en los casos anteriores, este nombre debería ser cambiado por un nombre descriptivo de su aplicación.
    - Dentro de este directorio encontraremos los archivos:
        - *admin.py*: el *rest_framework* de Django posee una herramienta que podría permitirnos hacer *CRUD* de nuestro modelo de datos y en este archivo registramos los elementos de nuestro modelo para permitirle realizar este proceso.
        - *apps.py*: Permite definir configuraciones específicas y metadatos de nuestra aplicación.
        - *models.py*: Permite definir el *MODELO DE DATOS* que soportará nuestra aplicación. Contiene clases que representan tablas de nuestra base de datos y que serán mapeadas por nuestro ORM (Object Relational Mapping).
        - *tests.py*: Acá podremos definir nuestros *TESTS UNITARIOS* para validar automáticamente la lógica de nuestra aplicación, los modelos y las vistas.
        - *views.py*: Este el núcleo de nuestra aplicación, el *CONTROLADOR*. Acá tendremos la lógica que procesará una solicitud o *REQUEST* enviada a nuestra APP y enviará la respectiva respuesta o *"RESPONSE"*. Esta estructura de trabajo responde al patrón de diseño *Modelo Vista Controlador*, obteniendo data de los modelos, aplicando la lógica y renderizando una vista para mostrar esa respuesta.
    - Cuando la estructura de archivos de la aplicación ya ha sido generada, podemos iniciar el servidor de la aplicación, ejecutando el siguiente comando en el terminal:
        ```
        python manage.py runserver
        ```

    - Este comando inicia el servidor, el que se carga en la url http://127.0.0.1:8000.

6. **Plantillas Base**

    Las plantillas base permiten crear un esqueleto de diseño común para todas las páginas de una aplicación, evitando la repetición de código HTML y manteniendo la consistencia visual. Esto se logra creando un archivo HTML base que contiene bloques de contenido dinámico, y luego extendiendo esta plantilla en otras páginas para rellenar esos bloques con contenido específico de cada vista.
    - Dentro del directorio de nuestra aplicación, crearemos un nuevo directorio llamado *templates*, donde pondremos todas las vistas de nuestra aplicación.
    - Crear un archivo HTML de plantilla base en la carpeta *mi_aplicacion/templates* recién creada, puede llamarse *base.html*.
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
    
    -  Dentro de la plantilla base, se utilizan etiquetas como {%block nombre_bloque %} y {% endblock %} para definir áreas de contenido que pueden ser reemplazadas en las vistas que heredan de ella.
    - Las vistas extienden desde la plantilla base utilizando la sintaxis {% extends "plantilla_base.html" %}.
        ```html
        {% extends "base.html" %}
        
        {% block titulo %}Página de Inicio{% endblock %}
        
        {% block titulo_encabezado %}¡Bienvenido a mi sitio!{%endblock %}
        
        {% block contenido %}
        <p>Este es el contenido específico de la página de inicio.</p>
        {% endblock %}
        ```


7. **Modificando la página de inicio**
    - Por defecto cuando iniciamos el servidor, carga una página con información de Django, pero no es lo que debiéramos ver cuando cargamos una aplicación, por lo que cambiaremos la página de inicio.
    - Primero debemos indicarle a Django que el directorio de nuestra aplicación contiene una APP, agregamos nuestra APP a la lista INSTALLED_APPS  de *motor_django/settings.py*:
        ```
        INSTALLED_APPS = [
            # apps de django
            'mi_aplicacion',
        ]
        ```

    - Dentro del subdiretorio *mi_aplicacion/templates* creamos la vista HTML que será renderizada por el método creado anteriormente, la que llamaremos *bienvenida.html*.
    - Dentro de este archivo, pondremos el código HTML de nuestra página de bienvenida.
    - En el archivo *mi_aplicacion/views.py* generamos el método que renderizará la vista creada:
        ```
        from django.shortcuts import render

        def bienvenida(request):
            return render(request, 'bienvenida.html')
        ```

    - Luego debemos importar las vistas desde nuestra app en *motor_django/urls.py* y llamar al método que renderizará esa vista:
        ```
        from mi_aplicacion import views

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('', views.bienvenida, name='bienvenida'),
        ]
        ```

    - Esta ruta o *PATH* recibe 4 argumentos:
        - Ruta(string): Obligatorio. Patrón URL usado para identificar la ruta indicada en la aplicación. En este caso es '', una ruta vacía, o el inicio de nuestra APP, después del nombre del servidor *http://127.0.0.1:8000/*.
        - Vista(function): Obligatorio. Función que se llamará al cargar esa URL en la aplicación, la que debería existir en *mi_aplicacion/views.py*. En este caso llamaremos a la función *bienvenida*.
        - Argumentos(Dictionary): Opcional. Argumentos que se enviarán a nuestra función. 
        - name(string): Opcional. Nombre que le daremos a nuestro patrón URL. En este caso lo llamaremos *'bienvenida'* y de esa forma podemos llamarlo por nombre en la barra de navegación.

    - Cuando iniciemos nuevamente nuestro servidor, debiera cargar la vista recién creada en lugar de la vista Django por defecto.

8. **Página de Error 404 Genérica**
    - Si python NO encuentra un recurso (página) solicitado, arrojará una página de error con información del servidor, lo que involucra un serio problema de seguridad. Para evitarlo, debemos cargar un página genérica de error, lo que lograremos de la siguiente forma:
        - Deshabilitamos el modo de pruebas de nuestra aplicación en *motor_django/settings.py*:
            ```
            DEBUG = False
            ```

        - Cuando el modo de pruebas se ha deshabilitado, ya no se verá la información del servidor al tratar de cargar un recurso que no existe, sino una página de Django que dice:
            ```
            Not Found
            The requested resource was not found on this server.
            ```

        - Si la aplicación NO esta corriendo en modo de prueba, implica que está en modo productivo, lo que nos debería indicar que nuestro servidor local no debería funcionar. Para resolver esto, debemos AUTORIZAR nuestro servidor local, para permitirle que funcione en modo de producción, modificando *motor_django/settings.py*:
            ```
            ALLOWED_HOSTS = ['localhost','127.0.0.1']
            ```

        - Para que se muestre una página de error creada por nosotros, dentro del directorio *templates* creado anteriormente, crearemos un archivo *html* de nombre *404*. Django buscará en este directorio ese archivo y lo cargará al no encontrar un recurso.

9 **Manejo de Archivos Estáticos**
    Para cargar y usar tus propios archivos estáticos (CSS, JavaScript, imágenes) en Django, sigue estos pasos básicos.
    - Asegúrate de que en tu archivo *motor_django/settings.py* esté configurado el STATIC_URL y la ruta donde Django buscará los archivos:
        ```
        STATIC_URL = 'static/'

        # Opcional: Directorios globales adicionales para archivos estáticos
        STATICFILES_DIRS = [
            BASE_DIR / "static",
        ]
        ```
    
    - Puedes poner tus archivos estáticos en un directorio dentro de tu aplicación o en la carpeta raíz del proyecto, creando un directorio *static* y dentro de ese directorio, generar los que sean necesarios para mantener el orden del sistema y separar distintos tipos de archivos.

10. **Manejo de Base de Datos**

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

    - ORM: Para comunicarnos con la DB usaremos un ORM (*Object Relational Mapping*), que se encargará de entender los objetos (por el lado del código) y las entidades (por el lado de la base de datos). 

        | Código |          | Base de datos |
        | -------- | -------- | -------- |
        | Clase | <------> | Entidad |
        | objeto | <------> | registro |

    - Usaremos *SqlAlchemy* como *ORM*, junto con el driver de base de datos *mysqlclient*, los que se instalarán mediante la ejecución del siguiente comando en el terminal:
        ```
        pip install SQLAlchemy mysqlclient
        ```

    - Una vez con la base de datos creada, procedemos a modificar nuestro archivo settings.py. Indicamos que haremos uso del gestor MySQL, en vez de SQLite que usa por defecto Django, modificando la sección *DATABASES* del archivo *motor_django/settings.py*:
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

11. **Modelo de Datos**
    - Django controlará la base de datos mediante migraciones, scripts de bases de datos que modificarán la estructura de datos.
    - Django maneja varias tablas de manera predeterminada para información interna, para que se creen en la DB, debemos ejecutar el comando:
        ```
        python manage.py migrate
        ```

    - Este comando aplicó una serie de migraciones nativas de Django en la base de datos, como permisos, usuarios, autorizaciones, sesiones, etc...
    - El siguiente paso es aplicar NUESTRO modelo a la base de datos. Para crear los modelos debemos modificar el archivo *mi_aplicacion/models.py* y agregar las *clases* que hemos determinado para nuestro proyecto. Idealmente debiéramos tener un diagrama entidad-relación o uno de clases para tener claro el modelo de datos.
    - Nuestras clases se crearán heredando desde *models* de Django, para poder acceder a los ditintos tipos de datos que deberá tener como atributos.
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
    
    - Cada tipo de dato heredado desde *models* tiene algunos argumentos, los que pueden ser comunes, aplicacbles a cualquier tipo de dato, o específicos, que dependen del tipo de campo:
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

12. **Datos Iniciales de la Aplicación**

    Al estar definida nuestra base de datos y aplicadas las migraciones de nuestro modelo de datos, tenemos la estructura de datos requerida para alojar nuestros registros.
    En este punto será importante contar con datos genéricos iniciales de la aplicación, como listas o parámetros que deben estar pre-cargados.
    Esto lo lograremos de la siguiente forma:
    - Dentro del directorio de nuestra aplicación crearemos un nuevo directorio *fixtures* que es donde guardaremos los archivos con datos en formato *JSON* para que sean cargados en la DB.
    - Para cada dato requerido generaremos un archivo *.json* que contendrá los datos necesarios.
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
    
    Donde *"pk"* es el campo *id* generado de manera automática por Django y *fields* serán los atributos de nuestro modelo.

13. **Desacoplar Datos Sensibles**

    Ahora que ya estamos trabajando con una DB externa, debemos usar credenciales para conectarnos a esta nueva DB. Cualquier credencial o dato sensible no debería existir en código, incluyendo la *'SECRET_KEY'* de Django, por lo que debemos *DESACOPLAR* esos datos y ponerlos en un archivo de ambiente.
    - Instalamos la librería *decouple* para desacoplar los datos y posteriormente leerlos desde un archivo de ambiente. El siguiente comando será necesario para instalar la librería:
        ```
        pip install python-decouple
        ```

    - Creamos un archivo *.env* (archivo de ambiente, env de environment) en el directorio principal de la aplicación o donde se encuentre su archivo *manage.py*.
    - En el archivo *.env* ponemos los datos sensibles en variables que tendrán como valor el dato. Es importante no dejar espacios entre el nombre de la variable y la asignación del valor:
        ```
        SECRET_KEY='cadena_de_caracteres_django_secret_key'
        ```

    - Donde necesitemos usar ese dato, generalmente en *setting.py*, importaremos el método *config* de la librería *decouple* para acceder a los datos almacenados en el archivo de ambiente, de la siguiente forma:
    *settings.py*
        ```
        from decouple import config

        SECRET_KEY = config('SECRET_KEY')
        ```

    El método *config* traerá el valor de la variable almacenada en el archivo de ambiente que tenga el nombre que le pasamos al método como argumento.
    El mismo procedimiento debemos usar para procesar la información de la base de datos.

14. **Instalación Django Rest Framework**

    Django Rest Framework es una librería que contiene muchas herramientas que usaremos en nuestro desarrollo django, como los serializadores.
    Para instalarlo ejecutaremos el siguiente comando mediante terminal:
        ```
        pip install djangorestframework
        ```

    Una vez que se ha instalado, debemos agregarlo a la lista de *INSTALLED_APPS* en *settings.py* de nuestro motor Django.
        ```
        INSTALLED_APPS = [
            ...
            'rest_framework',
            ...
        ]
        ```
    
15. **Incorporar Modelo de Datos al administrador de Django**

    En el archivo *mi_aplicacion/admin.py* debemos *REGISTRAR* nuestro modelo de datos, para que el admin de django pueda procesar los datos.
    Esto lo lograremos de la siguiente forma:
    *admin.py*
        ```
        from django.contrib import admin
        from .models import MiClase
        from .models import MiClase2

        # Register your models here.
        admin.site.register(MiClase)
        admin.site.register(MiClase2)
        ```

16. **Creación de Serializadores**

    La librería *rest_framework* que instalamos anteriormente, tiene la herramienta para serializar nuestro modelo de datos en formato *JSON*, que será necesario para trabajar los datos en la aplicación web, lo que lograremos siguiendo estos pasos:
    - Primero crearemos un archivo *serializer.py* en el directorio de nuestra aplicación.
    - En el archivo creado, importaremos *serializers* para usarlos en la serialización de nuestro modelo.
    - Junto con esto, debemos importar todo nuestro modelo de datos desde *models.py*.
    - Finalmente, crearemos una clase que se encargará de serializar cada uno de nuestros modelos de datos.

    El archivo debiera quedar como el siguiente ejemplo:
        ```
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
        ```

17. **Creación de Vistas CBV**

    CBV es el acrónimo de Class Based View o *Vista Basada en Clase*, es una colección de vistas basadas en un modelo de datos y que nos permiten hacer *CRUD* de los datos de ese modelo.
    Las vistas basadas en clase se crearán dentro de *mi_aplicacion/views.py*, nuestro archivo controlador, siguiendo las siguientes instrucciones:
    - Importamos todos nuestros modelos de datos al archivo *views.py*.
    - Junto con la importación de las clases, importamos nuestros serializadores, puesto que se ancargarán de dejar los datos en un formato que podamos usar en las vistas.
    - con todo esto ya podemos crear nuestro *ViewSet*, o colección de vistas para trabajar con los datos del modelo desde Django Admin.

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

    Los ViewSet que creamos en el paso anterior generan las vistas y métodos para hacer el *CRUD* de nuestros datos con métodos *HTTP/S* de tipo *POST*, *GET*, *PUT/PATCH* o *DELETE*, pero ahora necesitamos llegar hasta esos métodos o *END-POINTS*, por lo que debemos generar las rutas necesarias.
    - En el directorio de nuestra aplicación creamos un nuevo archivo *urls.py*, donde gestionaremos todas las rutas necesarias para nuestro modelo de datos completo.
    - Dentro de este archivo, generaremos un objeto *enrutador* (routers.DefaultRouter) que se encargará de generar las rutas para los métodos mencionados. 
    - Para crear las rutas usaremos el método *register* disponible dentro del objeto enrutador. Este método recibe como primer argumento el nombre que le daremos al conjunto de rutas de un *ViewSet* y como segundo argumento le indicaremos cuál será el ViewSet que registraremos, por lo que el archivo quedará de la siguiente forma:
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

    - La *r* delante del string para generar la ruta es para evitar saltos de línea generados cuando se crea la ruta, es un tipo de dato *RAW* de Python.
    - El *urlpatterns* incluirá todas las rutas generadas dentro del enrutador y será necesario para enviarlas a *motor_django/urls.py*.

19. **Incorporación de rutas a Django**

    - Para que las rutas generadas en la aplicación queden disponibles dentro de *django/urls.py*, debemos importarlas e incluirlas, de la siguiente forma:
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
    
    - Con todo lo anterior, ya podemos iniciar nuestra aplicación, dirigirnos a: *http://127.0.0.1:8000/mi_aplicacion/* y comenzar a hacer *CRUD* de nuestros modelos.

20. **Inicio de Sesión con Django**

    El sistema de autenticación incluido con Django se centra en el modelo User, lo que permite manejar cuentas de usuario, permisos, y tareas esenciales como login, logout, y control de contraseñas.

    ### Extensión de User
    Podemos crear nuestro propio modelo de usuario, pero si usamos el nativo podemos mantener todo el sistema de autenticación (como el inicio de sesión con login(), contraseñas, permisos) y, al mismo tiempo, agregar nuestros propios campos personalizados. La mejor práctica para lograrlo es extender el modelo de usuario utilizando AbstractUser, de la siguiente forma:
    - Debemos definir el modelo personalizado en el archivo *mi_aplicacion/models.py*, y heredar de AbstractUser:
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

    - Debes indicarle a Django que use tu nuevo modelo en lugar del modelo por defecto. Añade la siguiente línea en tu archivo *motor_django/settings.py*:
        ```
        AUTH_USER_MODEL = 'mi_aplicacion.MiUsuario'
        ```

    - Para que puedas gestionar tus usuarios personalizados y ver tus nuevos campos desde el panel de administración de Django, usa *UserAdmin* para registrar tu modelo en *mi_aplicacion/admin.py*:
        ```
        from django.contrib import admin
        from django.contrib.auth.admin import UserAdmin
        from .models import MiUsuario

        # Esto asegura que los campos heredados y los nuevos se muestren correctamente
        admin.site.register(MiUsuario, UserAdmin)
        ```
___
**Crear un Usuario Admin de Django**

    El usuario *ADMIN* de Django es el que tendrá control administrativo de la aplicación y también podrá hacer *CRUD* de nuestro modelo de datos.
    Para crearlo, ejecutaremos el siguiente comando mediante nuestro terminal:
    ```
    python manage.py createsuperuser
    ```

    Una vez que jecutamos el comando, este nos pedirá la información del usuario mediante el mismo terminal.
___
**Control de Dependecias** 

Para poder mantener las librerias actualizadas y estandarizadas para todo el equipo de desarrollo, crearemos un archivo de requerimientos con el siguiente comando:
```
pip freeze > requirements.txt
```

Este archivo tendrá una lista de todas las librerías incluídas en nuestro *VENV*, las que posteriormente podrán ser instaladas en cualquier nuevo *VENV* ejecutando el siguiente comando:
```
pip install -r requirements.txt
```

> Cada vez que agreguemos una nueva librería actualizaremos el archivo de requerimientos con el comando *FREEZE*.
___
**Control de Fechas Global**

Si se necesita aplicar el mismo formato de fecha en toda la aplicación, debemos agregar un configuración global en *settings.py* como un diccionario llamado *REST_FRAMEWORK*.
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