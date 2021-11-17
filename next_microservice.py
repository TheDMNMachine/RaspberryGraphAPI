import requests

from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:damian@192.168.0.103:5432/postgres"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

from crud.models import Weather

session = SessionLocal()


def request_weather_station():
    r = requests.get('http://192.168.0.104:5000/weather').json()

    print(r)

    weather = Weather(temperature=r['temperature'],
                      pressure=r['pressure'],
                      humidity=r['humidity'],
                      timestamp=datetime.today(),
                      station_id=1)
    session.add(weather)
    session.commit()
    session.close()


if __name__ == "__main__":
    request_weather_station()