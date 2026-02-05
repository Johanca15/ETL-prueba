Prueba Tecnica - Analista ETL

El objetivo principal de esta prueba es implementar un proceso ETL en el que se utilicen herramientas como python, Aiven y postgreSQL.

# Que incluye:
- Creacion de tablas
- Limpieza de datos
- Carga ETL
- Creacion de vistas
- Control de versiones Github


# Tecnologias utilizadas:
- Python 3
- Pandas, SQLAlchemy
- PostgreSQL en Aiven
- Visual Studio Code
- Git, Github

# Entorno virtual

Para el desarrollo se utilizo un entorno virtual (.venv). Este directorio no se incluyo en el repositorio ya que esta excluido mediante el archivo '.gitignore'.

# Base de datos
Se utilizo PostgreSQL mediante Aiven. La conexion se realizo desde python utilizando la libreria SQLAlchemy donde se ejecutaron los scripts que crearon las tablas, el proceso ETL y generaron las vistas.

La base de datos utilizada es 'defaultb' en Aiven. Ejemplo del formato de conexion: postgresql://usuario:password@host:puerto/defaultdb?sslmode=require

# Dataset

Pasos:
1. Generar los datasets de los links suministrados 
2. Renombrar como edesur_cobros.csv al dataset de edesur
3. Renombrar como rnc.csv al dataset de DGII

Se generaron estos archivos en formato CSV y se almacenan localmente en la carpeta 'dataset/', no se incluyeron en el reporsitorio.
- https://datos.gob.do/dataset/edesur-cobros-rd-mm 
- https://dgii.gov.do/herramientas/consultas/Paginas/RNC.aspx

# Proceso ETL

1. Extraccion
- Se leyeron los dataset utilizando Pandas
- Se especifico un tipo de codificacion para evitar errores por caracteres especiales

2. Transformacion
 
- Se normalizaron los nombres en las columnas
- Conversion de tipo de datos (montos y anio)
- Se limpiaron los registros que eran tanto invalidos como nulos
- Eliminacion de duplicados 

3. Carga

- Creacion de las tablas en PostgreSQL si estas no existian
- Insercion de los datos a la base de datos


# Vistas

(EDESUR)
- Debido a que el dataser no contiene una columna explicita de provincia, la columna Zona de utilizo como referencia.
- Segmentaciones por zona y por anio
(DGII)
- Segmentacion por regimen y pago.

# Estructura

ETL_PRUEBA/
│
├── .venv/                         # Entorno virtual de Python (no se sube)
│
├── dataset/                       # Archivos CSV usados en el ETL (local)
│   ├── edesur_cobros.csv          # Datos de cobros de Edesur
│   └── rnc.csv                    # Listado de RNC de la DGII
│
├── sql/                           # Scripts Python que ejecutan SQL
│   ├── query+etl_EDESUR.py        # ETL de Edesur (crea tabla y carga datos)
│   ├── provincia_view.py          # Vista por zona/provincia (Edesur)
│   ├── query+etl_DGII.py          # ETL del RNC (crea tabla y carga datos)
│   └── regimen_pagos_view.py      # Vista por régimen y pagos (RNC)
│
├── README.md                      # Documentación del proyecto
├── .gitignore                     # Archivos excluidos del repositorio
├── conexion.py                    # Prueba de conexión a PostgreSQL (Aiven)

# PASO A PASO PARA EJECTURAR EL ETL:

Este proyecto no utiliza un archivo main.py.  
Cada script dentro de la carpeta `sql/` representa un proceso ETL o una consulta independiente.

1. Clonar el repositorio
2. Crear y activar un entorno virtual
3. Instalar las dependencias necesarias (pandas,sqlalchemy)
4. Configurar la conexión a la base de datos en `conexion.py`(debe colocar las credenciales suministradas al momento de crear una BD en Aiven, en este caso PostgreBD)
5. Tener descargados los datasets, explicado mas arriba
5. Ejecutar el script deseado o vista deseada

