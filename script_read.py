from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DB_CONFIG
from script import WeatherData

def display_weather_data(weather_data_list):
    for data in weather_data_list:
        print("Ciudad:", data.city)
        print("Fecha y Hora:", data.date_time)
        print("Temperatura:", data.temperature, "°C")
        print("Velocidad del viento:", data.wind_speed, "m/s")
        print("Latitud:", data.latitude)
        print("Longitud:", data.longitude)
        print("Descripción:", data.description)
        print("Día del Pronóstico:", data.forecast_day)
        print("------------------------------------")

def empty_database(session):
    confirmation = input("¿Estás seguro de que deseas vaciar la base de datos? (y/n): ")
    if confirmation.lower() == "y":
        session.query(WeatherData).delete()
        session.commit()
        print("Base de datos vaciada correctamente.")
    else:
        print("Operación cancelada.")

def main():
    engine = create_engine(DB_CONFIG['db_url'])
    Session = sessionmaker(bind=engine)
    session = Session()

    weather_data_list = session.query(WeatherData).all()

    display_weather_data(weather_data_list)

    action = input("¿Deseas vaciar la base de datos? (y/n): ")
    if action.lower() == "y":
        empty_database(session)

    session.close()

if __name__ == "__main__":
    main()
