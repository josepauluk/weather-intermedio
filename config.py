# Weather datos

#url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=49c13bdb94527dbe6310d58ea4765102&units=metric".format(city)

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
#BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "49c13bdb94527dbe6310d58ea4765102"

# Base de datos Postgres
BD = "weather"
USER = "postgres"
PASSWORD = "123456789"
HOST = "localhost"
PORT = 5432