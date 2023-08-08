# script.py

import requests
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DB_CONFIG, API_KEY, BASE_URL

Base = declarative_base()

class WeatherData(Base):
    __tablename__ = 'weather_data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String)
    date_time = Column(DateTime)
    temperature = Column(Float)
    wind_speed = Column(Float)
    latitude = Column(Float)
    longitude = Column(Float)
    description = Column(String)
    forecast_day = Column(DateTime)

# Obtener la entrada del usuario
city = input('Ingresa el nombre de la ciudad: ')

# Parámetros de la API
params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

# Obtener datos de la API
res = requests.get(BASE_URL, params=params)
data = res.json()

forecast_list = data.get("list", [])

# Configuración de la base de datos
engine = create_engine(DB_CONFIG['db_url'])
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

if not session.query(WeatherData).filter_by(city=city).first():
    print(f"Guardando datos para la ciudad: {city}")
    for forecast in forecast_list:
        # ... (resto de la lógica de procesamiento y almacenamiento de datos)
        # Obtener los valores del pronóstico para cada período
            date = datetime.fromtimestamp(forecast["dt"])
            temp = forecast["main"]["temp"]
            wind_speed = forecast["wind"]["speed"]
            description = forecast["weather"][0]["description"]
            latitude = data["city"]["coord"]["lat"]
            longitude = data["city"]["coord"]["lon"]
            
            # Obtener el día del pronóstico
            forecast_day = date  # Cambiamos forecast_day para que sea DateTime

            # Guardar los datos en la base de datos
            weather_data = WeatherData(
                city=city,
                date_time=date,
                temperature=temp,
                wind_speed=wind_speed,
                latitude=latitude,
                longitude=longitude,
                description=description,
                forecast_day=forecast_day
            )

            session.add(weather_data)

    session.commit()
    session.close()
    print("Datos guardados correctamente.")
else:
    print(f"Los datos para la ciudad {city} ya están guardados en la base de datos.")
