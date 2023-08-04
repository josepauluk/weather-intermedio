import requests
from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from config import BASE_URL, API_KEY, BD, USER, PASSWORD, HOST, PORT
from geopy.geocoders import Nominatim

Base = declarative_base()

class WeatherData(Base):
    __tablename__ = 'weather_data'
    id = Column(Integer, primary_key=True)
    city = Column(String)
    date = Column(DateTime)
    temperature = Column(Float)
    weather_description = Column(String)

def get_coordinates(city):
    geolocator = Nominatim(user_agent="weather_app")
    location = geolocator.geocode(city)

    if location:
        return location.latitude, location.longitude
    else:
        print(f"No se pudo encontrar la ubicación de '{city}'")
        return None, None

def get_weather_data(city):
    url = f"{BASE_URL}&q={city}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    print(data)  # Agregar esta línea para imprimir la respuesta

    try:
        city_name = data['name']
        date = datetime.fromtimestamp(data['dt'])
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']

        return city_name, date, temperature, weather_description

    except KeyError as e:
        print(f"Error al acceder a los datos del clima: {e}")
        return None


def save_to_database(data):
    engine = create_engine(f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{BD}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    city_name, date, temperature, weather_description = data
    weather_entry = WeatherData(city=city_name, date=date, temperature=temperature, weather_description=weather_description)

    session.add(weather_entry)
    session.commit()
    session.close()

if __name__ == "__main__":
    city_input = input("Ingrese el nombre de la ciudad para obtener los datos del clima: ")
    weather_data = get_weather_data(city_input)
    
    if weather_data:
        save_to_database(weather_data)
