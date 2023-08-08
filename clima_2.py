import requests
from datetime import datetime, timedelta
from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Definimos la clase para la tabla de la base de datos
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

API_KEY = "49c13bdb94527dbe6310d58ea4765102"
url = "https://api.openweathermap.org/data/2.5/forecast"

city = input('Enter City: ')

# Parámetros de la URL de la API para obtener el pronóstico a 5 días
params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

# Realizar la solicitud a la API de pronóstico a 5 días
res = requests.get(url, params=params)
data = res.json()

# Obtener los valores que nos interesan para cada período del pronóstico
forecast_list = data["list"]

# Guardamos los datos en la base de datos
engine = create_engine('postgresql://postgres:123456789@localhost:5432/weather_data')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

for forecast in forecast_list:
    # Obtener los valores del pronóstico para cada período
    date = datetime.fromtimestamp(forecast["dt"])
    temp = forecast["main"]["temp"]
    wind_speed = forecast["wind"]["speed"]
    description = forecast["weather"][0]["description"]
    latitude = data["city"]["coord"]["lat"]
    longitude = data["city"]["coord"]["lon"]

    # Guardar los datos en la base de datos
    weather_data = WeatherData(
        city=city,
        date_time=date,
        temperature=temp,
        wind_speed=wind_speed,
        latitude=latitude,
        longitude=longitude,
        description=description
    )

    session.add(weather_data)

session.commit()
session.close()
