# Pagina web de una empresa constructora

## Descripcion 
He intentado hacerlo todo en ingles pero lo he mezclado un poco
Proyecto final de DAW 1r curso utilizando tecnologías como: 
- html, css, js y jinja2 en frontend
- python y flask en backend
- mysql como base de datos

## Contenido principal

Este proyectos se basa en los siguientes puntos de navegación
- home
- proyectos
- proyectos por categorías
- proyecto
- nosotros
- servicios
- contacto
- login de cliente
- login de empleados

## librerías
Comando para instalar todas las librerías utilizadas
`pip install -r requirements.txt`

## datos adicionales 
esta el sql para crear el base de datos y en la carpeta inserts todos los inserts de las tablas
por si acaso o para evitar algún posible error que los inserts sean en orden, es decir, por ejemplo en traducciones.sql es importante que se inserten los valores por orden de inserts

Se han usado variables de entorno para la conexión a la base de datos y para la sesión 
en query.py se debe cambiar las lineas 11,12,13,14 por vuestros datos de conexión a la base de datos y en __init__.py en la linea 10 se debe cambiar su valor por una clave secreta puedes usar librerías propias de python como secrets`
`import secrets`
`secret_key = secrets.token_hex(32)`

también es importante mantener el orden de las imagenes, es decir, es decir, si quieres añadir imagenes que estén donde toca y no cambiar las imagenes predefinidas a otras rutas

Si quieres hacer pruebas individuales de las funciones de query.py en las funciones donde se llaman a los archivos json hay que cambiar la ruta app/json/name_projects.json a json/name_projects.json, ya que, cuando se ejecuta el run.py llama a esta ruta app/json/name_projects.json para encontrar al json pero si se ejecuta desde query.py no encuentra esa ruta porque esta en una carpeta anterior 

El archivo default_users_password.py tiene el usuario y contraseña que tienen asignado tanto los clientes como los empleados por defecto, sobre todo importante para las contraseñas porque estas se guardan hasheadas en la base de datos

## estado
Todavía esta en desarrollo pero esto es la entrega final de DAW 1r año