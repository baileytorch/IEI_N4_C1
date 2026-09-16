# IEI_N4_C1
Clases de Backend con Django

Como buenos desarrolladores, ya debemos tener creado un repositorio para trabajar el código de la aplicación que debemos construir.
- Si no ha trabajado aún con repositorios, he construido una pequeña guía paso a paso que está disponible en sus ambientes de aprendizaje.
- Cada estudiante debe construir un proyecto que se ha asignado con anterioridad. La lista de estudiantes con los proyectos asignados y la descripción de los proyectos, los puede encontrar en su ambiente de aprendizaje.

## Creación de Proyectos con Django

1. **Creación de Ambiente Virtual**
    - Un ambiente virtual mantendrá aislada toda la configuración de nuestro proyecto y su entorno de trabajo.
    - Habiendo creado nuestro repositorio, abrimos la carpeta contenedora en VS Code.</li>
    - Iniciamos un nuevo terminal, estando ubicados en el directorio principal.</li>
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
    cd nombre_ambiente\Scripts
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

    - El comando *cd..* permite salir de un directorio y ubicarnos en el superior, por lo que deberíamos ejecutarlo 2 veces para llegar al directorio principal, saliendo de *nombre_ambiente\Scripts*.

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

    - El comando anterior instaló todas las dependencias necesarias para que Django pueda trabajar, las que deberían haber quedado en *nombre_ambiente\Libs*. Estas debieran ser:
        - asgiref.
        - django.
        - sqlparse.
        - tzdata.
    - Ahora crearemos el entorno de trabajo de Django mediante el comando:
    ```
    django-admin startproject motor_django .
    ```

    - No debe olvidar el *PUNTO* al final del comando, para indicar que la carpeta de nuestro proyecto se debe crear en el directorio principal de trabajo.
    - Este comando creó la estructura de archivos de Django con nombre *motor_django*, el que Ud. puede cambiar al que guste. Debemos recordar que debe ser suficientemente descriptivo, por lo que es común usar el acrónimo *drf* que significaría *Django Rest Framework*.
    - Este directorio contiene los archivos de configuración de Django, dentro de los que tenemos. 
        - *settings.py*, contiene configuraciones generales, como la conexión a base de datos.
        - *urls.py*, contiene las rutas para redirigir las solicitudes *REQUEST* que lleguen a la aplicación.

5. **Creación de la Aplicación**
    - A continuación, para crear la aplicación que debemos construir, ejecutaremos el siguiente comando mediante terminal:
    ```
    django-admin startapp nombre_aplicacion
    ```

    - El comando anterior creó un nuevo directorio llamado *nombre_aplicacion*, igual que en los casos anteriores, este nombre debería ser cambiado por un nombre descriptivo de su aplicación.
    - Dentro de este directorio encontraremos los archivos:
        - *admin.py*: Django posee un administrador que podría permitirnos hacer *CRUD* de nuestro modelo de datos y en este archivo registramos los elementos de nuestro modelo para permitirle al admin de Django realizar este proceso.
        - *apps.py*: Permite definir configuraciones específicas y metadatos de nuestra aplicación.
        - *models.py*: Permite definir el *MODELO DE DATOS* que soportará nuestra aplicación. Contiene clases que representan tablas de nuestra base de datos y que serán mapeadas por nuestro ORM (Object Relational Mapping).
        - *tests.py*: Acá podremos definir nuestros *TESTS UNITARIOS* para validar automáticamente la lógica de nuestra aplicación, los modelos y las vistas.
        - *views.py*: Este el núcleo de nuestra aplicación. Acá tendremos la lógica que recibirá una solicitud o *"REQUEST"* enviada a nuestra APP y enviará la respectiva respuesta o *"RESPONSE"*. Esta estructura de trabajo responde al patrón de diseño *Modelo Vista Plantilla*, obteniendo data de los modelos, aplicando la lógica y renderizando una plantilla para mostrar esa respuesta.
    - Cuando la estructura de archivos de la aplicación ya ha sido generada, podemos iniciar el servidor de la aplicación, ejecutando el siguiente comando en el terminal:
    ```
    python manage.py runserver
    ```

    - Este comando inicia el servidor, el que se carga en la url http://127.0.0.1:8000.

6. **Modificando la página de inicio**
    - Por defecto cuando iniciamos el servidor carga una página con información de Django, pero no es lo que debiéramos ver cuando cargamos una aplicación, por lo que cambiaremos la página de inicio.
    - Primero debemos indicarle a Django que el directorio de nuestra aplicación contiene una APP, agregamos nuestra APP a la lista INSTALLED_APPS  de *motor_django/settings.py*:
    ```
    INSTALLED_APPS = [
        # apps de django
        'nombre_aplicacion',
    ]
    ```

    - En el directorio de nuestra app creamos un subdirectorio templates, donde pondremos nuestras vistas.
    - Dentro de este subdiretorio *nombre_aplicacion/templates* creamos la vista HTML que será renderizada por el método creado anteriormente, la que llamaremos *bienvenida.html*.
    - Dentro de este archivo, pondremos el código HTML de nuestra página de bienvenida.
    - En el archivo *nombre_aplicacion/views.py* generamos el método que renderizará la vista creada:
    ```
    def bienvenida(request):
        return render(request, 'bienvenida.html')
    ```

    - Luego debemos importar las vistas desde nuestra app en *motor_django/urls.py* y llamar al método que renderizará esa vista:
    ```
    from nombre_aplicacion import views

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', views.bienvenida, name='bienvenida'),
    ]
    ```

    - Esta ruta o *PATH* recibe 4 argumentos:
        - Ruta(string): Obligatorio. Patrón URL usado para identificar la ruta indicada en la aplicación. En este caso es '', una ruta vacía, o el inicio de nuestra APP, después del nombre del servidor *http://127.0.0.1:8000/*.
        - Vista(function): Obligatorio. Función que se llamará al cargar esa URL en la aplicación, las que deberían existir en *nombre_aplicacion/views.py*. En este caso llamaremos a la función *bienvenida* que creamos en *nombre_aplicacion/views.py*.
        - Argumentos(Dictionary): Opcional. Argumentos que se enviarán a nuestra función. 
        - name(string): Opcional. Nombre que le daremos a nuestro patrón URL. En este caso lo llamaremos *'bienvenida'* y de esa forma podemos llamarlo por nombre.

    - Cuando iniciemos nuevamente nuestro servidor, debiera cargar la vista recién creada en lugar de la vista Django por defecto.

7. **Página de Error 404 Genérica**
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

        - Para que se muestre una página de error creada por nosotros, debemos tener un directorio *templates* en nuestra aplicación y dentro de ese directorio un archivo *html* de nombre *404*. Django buscará en este directorio ese archivo y lo cargará al no encontrar un recurso.

8. **Modelo de Datos**
    - Django controlará la base de datos mediante migraciones, scripts de bases de datos que modificarán la estructura de datos.
    - Django maneja varias tablas de manera predeterminada para información interna, para que se creen en la DB, debemos ejecutar el comando:
    ```
    python manage.py migrate
    ```

    - Este comando aplicó una serie de migraciones nativas de Django en la base de datos, como permisos, usuarios, autorizaciones, sesiones, etc...
    - El siguiente paso es aplicar NUESTRO modelo a la base de datos. Para crear los modelos debemos modificar el archivo *nombre_aplicacion/models.py* y agregar las *clases* que hemos determinado para nuestro proyecto. Idealmente debiéramos tener un diagrama entidad-relación o uno de clases.
    - Nuestras clases se crearán heredando desde *models* de Django, para poder acceder a los ditintos tipos de datos que deberá tener como atributos.
    - Estructura de creación de una clase:
    ```
    class MiClase(models.Model):
        atributo_1 = models.CharField(max_length=25,null=false)
        atributo_2 = models.TextField(max_length=100,null=false)
        atributo_3 = models.DateField(null=false)
        atributo_4 = models.TimeField(null=false)
        atributo_5 = models.DateTimeField(max_length=100,null=false)
        atributo_6 = models.IntegerField()
        atributo_7 = models.DecimalField()
        atributo_8 = models.FloatField()
        atributo_9 = models.EmailField()
        atributo_10 = models.BooleanField(default=true)
        atributo_11 = models.URLField(default=true)
        created_at = models.DateTimeField(default=ahora)
        updated_at = models.DateTimeField(auto_now=True)

    class MiClase2(models.Model):
        atributo_referenciado = models.ForeignKey(MiClase,on_delete=CASCADE)
        atributo_2 = models.CharField(max_length=100)
        created_at = models.DateTimeField(default=ahora)
        updated_at = models.DateTimeField(auto_now=True)
    ```

    - Con nuestras clases ya creadas, debemos GENERAR una nueva migracion con el comando:
    ```
    python manage.py makemigrations
    ```

    - Una vez que se ha creado nuestra nueva migración, debemos aplicarla a la base de datos, ejecutando nuevamente el comando:
    ```
    python manage.py migrate
    ```

    >Cada vez que modifiquemos el modelo de datos, crearemos una nueva migración y la aplicaremos a la base de datos para que se actualice de acuerdo a nuestro modelo.

___   
> Para poder mantener las librerias actualizadas y estandarizadas para todo el equipo de desarrollo, crearemos un archivo de requerimientos con el siguiente comando:
```
pip freeze > requirements.txt
```

> Este archivo tendrá una lista de todas las librerías incluídas en nuestro *VENV*, la que podrá ser instalada en cualquier nuevo *VENV* ejecutando el siguiente comando:
```
pip install -r requirements.txt
```

> Cada vez que agreguemos una nueva librería actualizaremos el archivo de requerimientos con el comando *FREEZE*.