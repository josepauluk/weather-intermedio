import requests
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Definimos la clase para la tabla de la base de datos
class WeatherData(Base):
    __tablename__ = 'weather_data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String)
    date_time = Column(DateTime)  # Usamos DateTime en lugar de Date para forecast_day
    temperature = Column(Float)
    wind_speed = Column(Float)
    latitude = Column(Float)
    longitude = Column(Float)
    description = Column(String)
    forecast_day = Column(DateTime)  # Cambiamos la columna a DateTime

API_KEY = "49c13bdb94527dbe6310d58ea4765102"
url = "https://api.openweathermap.org/data/2.5/forecast"

city = input('Ingresa el nombre de la ciudad: ')

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
forecast_list = data.get("list", [])

if not forecast_list:
    print("No se encontraron datos de pronóstico para la ciudad especificada.")
else:
    # Guardamos los datos en la base de datos
    engine = create_engine('postgresql://postgres:123456789@localhost:5432/weather')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    if not session.query(WeatherData).filter_by(city=city).first():
        print(f"Guardando datos para la ciudad: {city}")
        for forecast in forecast_list:
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
