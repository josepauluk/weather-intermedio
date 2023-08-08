# Weather App

Esta aplicación utiliza la API de OpenWeatherMap para obtener datos climáticos de diferentes ciudades y los guarda en una base de datos PostgreSQL.

## Requisitos previos

Antes de utilizar esta aplicación, asegúrate de tener instalados los siguientes elementos:

- Python 3.x
- PostgreSQL

## Instalación

1. Clona este repositorio en tu máquina local: https://github.com/josepauluk/weather-intermedio.git
2. Accede al directorio del proyecto:
3. Instala las dependencias del proyecto:
4. Configura la base de datos PostgreSQL: (Debe tener un campo "ID" como primary key autoincremental)

   - Crea una base de datos llamada "weather_data".
   - Actualiza las variables de configuración en el archivo `config.py` con tus credenciales de PostgreSQL.
   Por ejemplo:
   # Archivo config.py

        '''
        BASE_URL = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        # API de José Pauluk real
        API_KEY = "49c13bdb94527dbe6310d58ea4765102"

        # Base de datos Postgres
        BD = "weather_data"
        USER = "postgres"
        PASSWORD = "xxxxxxxx"
        HOST = "localhost"
        PORT = 5432
        '''

## Uso

1. Ejecuta el programa principal main.py:
2. Sigue las instrucciones en pantalla para ingresar el nombre de la ciudad y obtener los datos climáticos.

## Contribución

Si deseas contribuir a este proyecto, sigue los siguientes pasos:

1. Haz un fork de este repositorio.
2. Crea una rama para tu nueva funcionalidad: `git checkout -b feature/nueva_funcionalidad`.
3. Realiza los cambios necesarios y realiza los commits: `git commit -m "Agrega nueva funcionalidad"`.
4. Envía tus cambios al repositorio remoto: `git push origin feature/nueva_funcionalidad`.
5. Abre una solicitud de extracción en GitHub.

## Licencia

Este proyecto está bajo la Licencia MIT. Puedes consultar el archivo [LICENSE](LICENSE) para más detalles.

