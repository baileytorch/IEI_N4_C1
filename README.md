# IEI_N4_C1
Clases de Backend con Django

## Proyectos Backend con Django
1. **Creación del Ambiente (environment) Virtual.**

    El ambiente virtual permite mantener aislado el desarrollo de cada proyecto y sus configuraciones.
    - Teniendo creado el directorio de nuestro proyecto (repositorio clonado), iniciamos un nuevo terminal.
    - Para crear el ambiente virtual, ejecutamos el siguiente comando en nuestro terminal:
    ```
    python -m venv nombre_ambiente
    ```

2. **Activación del Ambiente Virtual.**
    
    El ambiente virtual debe permanecer activo durante todo el tiempo de desarrollo, para mantener aislada la configuración y los cambios efectuados en el ambiente.
    - Mediante el terminal nos ubicamos dentro del directorio creado con la instrucción anterior.
    - Dentro de este directorio, nos movemos al subdirectorio Scripts.
    - Dentro de Scripts, ejecutamos el siguiente comando en nuestro terminal:
    ```
    .\Activate
    ```
    - Si obtenemos un error de permisos para ejecutar scripts, le daremos permisos especiales a nuestro terminal mediante la siguiente instrucción:
    ```
    Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
    ```
    - Una vez otorgados los permisos, podemos volver a ejecutar el comando anterior.

    - Si trabajamos en varios proyectos y debemos cambiar de un ambiente a otro, desactivaremos el ambiente con el siguiente comando:
    ```
    deactivate
    ```

3. **Creación del Núcleo de Django**
    - Para trabajar con Django debemos crear la estructura de directorios y la instalación de las dependencias iniciales.
    - Debemos ubicarnos en la carpeta raíz del proyecto y crearemos un nuevo proyecto Django con el siguiente comando:
    ```
    pip install django
    ```
    - Ahora que las dependencias de Django ya han sido instaladas, crearemos nuestro primer proyecto Django, ejecutando el siguiente comando:
    ```
    django-admin startproject nombre_django .
    ```
    - nombre_django debe ser reemplazado por el nombre que Ud. le dará a su motor Django, es común que se use el acrónimo drf (Django Rest framework). Idealmente debe ser un nombre corto, porque deberemos llamarlo en más de alguna oportunidad.

4. **Creación de Aplicación**
    - Cuando ya tenemos un motor Django funcional, podemos crear nuestra aplicación particular que contendrá los controladores, las vistas y los modelos.
    - Para crear nuestra aplicación, nos ubicamos mediante el terminal en la carpeta raíz del proyecto y ejecutamos el siguiente comando:
    ```
    django-admin startapp nombre_aplicacion
    ```
    - nombre_aplicacion debe ser reemplazado por el nombre que Ud. le dará a su aplicación, el que debe ser descriptivo para seguir normativas de buenas prácticas.
    - Una vez creada la aplicación, debemnos agregar el nombre de la aplicación a la lista de INSTALLED_APPS de setting.py de nuestro núcleo django.
    - Ya creada la aplicación, iniciamos el servidor para confirmar que todo está funcionando OK.
    - El servidor se inicia con el siguiente comando mediante terminal:
    ```
    python manage.py runserver
    ```
    - Si todo ha funcionado de manera correcta, debiera cargar una vista genérica de Django al iniciar el servidor.