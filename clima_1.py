import requests
from sqlalchemy import create_engine, Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Definimos la clase para la tabla de la base de datos
class WeatherData(Base):
    __tablename__ = 'weather_data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String)
    temperature = Column(Float)
    wind_speed = Column(Float)
    latitude = Column(Float)
    longitude = Column(Float)
    description = Column(String)

API_KEY = "49c13bdb94527dbe6310d58ea4765102"
url = "https://api.openweathermap.org/data/2.5/weather"

city = input('Enter City: ')

# Parámetros de la URL de la API
params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

# Realizamos la solicitud a la API
res = requests.get(url, params=params)
data = res.json()

# Obtenemos los valores que nos interesan
temp = data["main"]["temp"]
wind_speed = data["wind"]["speed"]
latitude = data["coord"]["lat"]
longitude = data["coord"]["lon"]
description = data["weather"][0]["description"]

print("Temperatura: ", int(temp), "°C")
print("Velocidad del viento: ", wind_speed, "m/s")
print("Latitud: ", latitude)
print("Longitud: ", longitude)
print("Descripción: ", description)

# Guardamos los datos en la base de datos
engine = create_engine('postgresql://postgres:123456789@localhost:5432/weather')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

weather_data = WeatherData(
    city=city,
    temperature=temp,
    wind_speed=wind_speed,
    latitude=latitude,
    longitude=longitude,
    description=description
)

session.add(weather_data)
session.commit()

session.close()
