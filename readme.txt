# Sistema Escolar 3172141

[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)

## Configuración del Entorno (.env)

### Paso a Paso para Crear el Archivo .env

1. **Crear el archivo** en la raíz del proyecto:
```bash
touch .env
```
2. **Abrir el archivo** con tu editor favorito:
```bash
vim .env
```
3. **Copiar y pegar** las variables de enorno:
```
# ============================================
# DJANGO CONFIGURATION
# ============================================
SECRET_KEY=tu_clave_secreta_muy_segura_aqui_cambiar_por_una_real
DEBUG=True

# ============================================
# POSTGRESQL DATABASE
# ============================================
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
```
## Configuración del Proyecto

### Paso a Paso para correr el aplicativo

Nota para este instructivo:
      Se asume que se tienen instalados, o se instalarán -
      el lenguaje de programación Python versión 3.13.5 o superior, el SGBD MySQL 
      y la interfaz gráfica 'Workbench'.  Para otro SGBD se deben instalar las herramientas
      gráficas necesarias para la creación de la base de datos y realizar los
      cambios necesarios en el archivo 'settings.py' en el diccionario 'DATABASES' 
      así como también realizar la descarga del paquete necesario para la gestión 
      del SGBD desde el lenguaje.

      Se utiliza la GUI Workbench como la herramienta principal de MySQL, pero
      también se puede utilizar HeidiSQL, XAMPP o WAMPP que también son para MySQL.

Antes de iniciar el aplicativo realizar los siguientes pasos:

**1. Creación de la base de datos MySQL** En Workbench:
   - En el menú 'File' seleccionar: 'Open SQL Script...'
   - En la ventana de dialogo modal 'Open SQL Script': Ubicarse en la carpeta 
     'C:\...\sistema_escolar_3172141>',
     donde 'C:\...\' es la ruta donde se encuentra la carpeta principal, y
     seleccionar el archivo 'script_creacion_bd.txt'.
     NOTA: si no aparece el archivo debe seleccionar 'All Files (*.*)'
           del cuadro de selección que se encuentra al lado derecho del
           cuadro de nombre de archivo de la ventana de dialogo.
   - Una vez cargado el archivo ejecutar el script con la herramienta  
     'Execute the selected portion of...' que es un rayo amarillo al lado de 
     las herramientas 'abrir' y 'guardar' de la pestaña.

   - Una vez creada la base de datos con sus respectivas tablas, abrir y ejecutar 
     el script 'script_inserciones.txt' de la misma forma que se abrió y ejecutó 
     el script 'script_creacion_bd.txt'.

**2. Creación del ambiente virtual**
   En VS Code:
   - Abrir una terminal 'Command Prompt'
   - En la carpeta raíz 'sistema_escolar_3172141' ejecutar
     el comando 'python -m venv envse' sin las comillas, 
     o con el comando 'py -m venv envse' sin las comillas.
   - Una vez creado el ambiente virtual se debe activar
     con el siguiente comando 'envse\scripts\activate' sin las comillas
     debe aparecer algo parecido a '(envse) C:\...\sistema_escolar_3172141>'
     donde 'C:\...\' es la ruta donde se encuentra la carpeta principal
   - Actualizar 'pip' con el comando 'python -m pip install --upgrade pip'
     o con el comando 'py -m pip install --upgrade pip' sin las comillas
   - Instalar el framework y el controlador de la base de datos con 
     el comando 'pip install -r requirements.txt' sin las comillas

**3. Realizar migración a la base de datos de las tablas**
   - en el Command Prompt ejecutar el comando:
        ```bash
        python manage.py makemigrations
        ```

   - en el Command Prompt ejecutar el comando:
        ```bash
        python manage.py migrate
        ```

**4. Crear los modelos a partir de las tablas de la bd:**
   - En el Command Prompt ejectuar el comando:

        ```bash
        python manage.py inspectdb paises departamentos ciudades
      tipos_documento generos estratos estado_civil nivel_educativo
      aulas areas grados asignaturas grupos roles usuarios temas
      perfil_usuario > se_core/models.py
        ```


**5. Crear el superusuario de django**
   - en el Command Prompt ejecutar el comando:

        ```bash
        python manage.py createsuperuser
        ```
     y digitar los campos solicitados.  Cuando se solicita la contraseña no va 
     a visualizar lo que esté digitando por lo que es muy importante que
     recuerde el orden de las teclas que presiona y no olvidar que la contraseña
     queda cifrada sin posibilidad de recuperación.

**6. Estructura del proyecto:**
   notación * (d): directorio o carpeta
            * (a): archivo
   |- (d) sistema_escolar_3172141
          |- (d) envse
          |- (d) se
                 |- (d) __pycache__
                 |- (a) __init__.py
                 |- (a) asgi.py
                 |- (a) settings.py
                 |- (a) urls.py
                 |- (a) wsgi.py
          |- (d) se_core
                 |- (d) __pycache__
                 |- (d) media
                 |- (d) migrations
                 |- (d) static
                        |- (d) css
                               |- (a) aside_coordinador.css
                               |- (a) bootstrap.min.css
                        |- (d) img
                        |- (d) js
                               |- (a) bootstrap.bundle.min.js
                 |- (d) templates
                        |- (d) includes
                               |- (a) aside_coordinador.html
                               |- (a) aside_docente.html
                               |- (a) footer.html
                               |- (a) navbar.html
                        |- (d) se_core
                               |- (a) acerca_de.html
                               |- (a) contactanos.html
                               |- (a) index.html
                               |- (a) login_frm.html
                               |- (a) mision.html
                               |- (a) registro.html
                        |- (a) base.html
                        |- (a) inicio.html
                 |- (d) vistas
                        |- coordinador
                        |- navegacion
                 |- (a) __init__.py
                 |- (a) admin.py
                 |- (a) apps.py
                 |- (a) forms.py
                 |- (a) models.py
                 |- (a) tests.py
                 |- (a) urls.py
                 |- (a) views.py
          |- (a) .gitignore
          |- (a) manage.py
          |- (a) readme.txt
          |- (a) requirements.txt
          |- (a) script_creacion_bd.txt
          |- (a) script_inserciones.txt