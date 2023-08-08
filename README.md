# Weather Forecast - Intermedio - para proyecto final Informatorio

Esta es una aplicación para obtener pronósticos del clima y almacenarlos en una base de datos. Utiliza la API de pronóstico del clima (https://openweathermap.org/) para obtener datos y SQLAlchemy para gestionar la base de datos.

## Requisitos Previos

Antes de comenzar, asegúrate de tener lo siguiente instalado:

- Python (versión 3.6 o superior)
- pip (el gestor de paquetes de Python)
- Una clave de API de pronóstico del clima (puedes obtenerla registrándote en el servicio de pronóstico del clima: https://openweathermap.org/)

## Instalación

1. Clona este repositorio:
git clone https://github.com/josepauluk/weather-intermedio.git


2. Ve al directorio del proyecto:
cd weather-intermedo


3. Crea un entorno virtual:
virtualenv venv


4. Instala las dependencias:
pip install -r requirements.txt


## Configuración

Crea un archivo `config.py` en el directorio del proyecto. Define las siguientes variables:


```python 
API_KEY = "TU_CLAVE_DE_API"
BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"

DB_CONFIG = {
        # Por ejemplo: 'db_url': 'postgresql://postgres:123456789@localhost:5432/weather'
    'db_url': 'URL_DE_LA_BASE_DE_DATOS'
}

Sustituye TU_CLAVE_DE_API, URL_DE_LA_API_DE_PRONÓSTICO y URL_DE_LA_BASE_DE_DATOS con tus valores reales.

Uso
Ejecuta el script.py para obtener pronósticos y guardarlos en la base de datos:


Ejecuta script_read.py
Para ver los datos almacenados en la base de datos. También puedes optar por vaciar la base de datos desde este script.

Contribución
Si deseas contribuir a este proyecto, ¡estaré encantado de recibir tus pull requests!

Licencia
Este proyecto está bajo la Licencia MIT.
