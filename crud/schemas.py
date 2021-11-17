from typing import List, Optional
from datetime import datetime

from pydantic import BaseModel


class WeatherBase(BaseModel):
    temperature: float
    pressure: float
    humidity: float


class Weather(WeatherBase):
    id: int
    timestamp: datetime
    station_id: int

    class Config:
        orm_mode = True


class CreateWeather(WeatherBase):
    pass


class BaseStation(BaseModel):
    type_of_station: str


class Station(BaseStation):
    name: str
    weather: List[Weather] = []

    class Config:
        orm_mode = True


class CreateStation(BaseStation):
    name: str
