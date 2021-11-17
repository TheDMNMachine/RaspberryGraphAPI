from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas, crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/stations/", response_model=schemas.Station)
def create_station(station: schemas.CreateStation, db: Session = Depends(get_db)):
    db_station = crud.get_station_by_name(db, name=station.name)
    if db_station:
        raise HTTPException(status_code=400, detail="Name already used")
    return crud.create_station(db=db, station=station)


@app.get("/stations/", response_model=List[schemas.Station])
def read_stations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    stations = crud.get_stations(db, skip=skip, limit=limit)
    return stations


@app.get("/stations/{station_id}", response_model=schemas.Station)
def read_station(station_id: int, db: Session = Depends(get_db)):
    db_station = crud.get_station(db, station_id=station_id)
    if db_station is None:
        raise HTTPException(status_code=404, detail="Station not found")
    return db_station


@app.post("/stations/{station_id}/weather/", response_model=schemas.Weather)
def create_weather_from_station(
    station_id: int, weather: schemas.CreateWeather, db: Session = Depends(get_db)
):
    return crud.create_station_weather(db=db, weather=weather, station_id=station_id)


@app.get("/weather/", response_model=List[schemas.Weather])
def read_weathers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    weathers = crud.get_weathers(db, skip=skip, limit=limit)
    return weathers