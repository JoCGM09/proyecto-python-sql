# proyecto-python-sql
Proyecto: Traer datos de una API en JSON, convertir la información a data estructurada y almacenarla en una base de datos SQL en la nube
TODO:
- Crear el entorno virtual (DONE)
- Encontrar una API y extraer datos
- Crear una conexión a la base de datos

## Creación de un entorno virtual

python -m venv venv

con este comando creas el entorno virtual en el directorio actual llamado venv.

source venv/Scripts/activate

con este comando activas el entorno virtual

which python

con este comando te aseguras de tener activo el entorno virtual

pip install json requests psycopg2-binary

con este comando instalas las dependencias necesarias para los proyectos

pip list

con este comando ves la lista de paquetes instalados dentro de este entorno virtual

pip freeze

este comando te da los paquetes en el formato necesario para un archivo requirements.txt

pip freeze > requirements.txt

este comando genera el archivo requirements.txt con los paquetes

deactivate

nota: este comando desactiva el entorno virtual, para eliminar el ambiente completo, debes eliminar el archivo

para usar las librerías del proyecto usar

pip install -r requirements.txt

## Manejo de APIs

La librería requests nos permite trabajar facilmente con APIs y con peticiones HTTP en general. Revisar el archivo de requestsNotes.py

## Manejo de JSON

La librería json nos permitirá manipular el formato json. Revisar el archivo de jsonNotes.py

