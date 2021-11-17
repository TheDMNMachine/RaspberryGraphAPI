from sqlalchemy.orm import Session

from . import models, schemas

from datetime import datetime


def get_station(db: Session, station_id: int):
    return db.query(models.Station).filter(models.Station.id == station_id).first()


def get_station_by_name(db: Session, name: str):
    return db.query(models.Station).filter(models.Station.name == name).first()


def get_stations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Station).offset(skip).limit(limit).all()


def create_station(db: Session, station: schemas.CreateStation):
    name = station.name
    db_station = models.Station(name=station.name, type_of_station=station.type_of_station)
    db.add(db_station)
    db.commit()
    db.refresh(db_station)
    return db_station


def get_weathers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Weather).offset(skip).limit(limit).all()


def create_station_weather(db: Session, weather: schemas.CreateWeather, station_id: int):
    db_weather = models.Weather(**weather.dict(), station_id=station_id, timestamp=datetime.today())
    db.add(db_weather)
    db.commit()
    db.refresh(db_weather)
    return db_weather
