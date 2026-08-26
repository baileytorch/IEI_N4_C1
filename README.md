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
    