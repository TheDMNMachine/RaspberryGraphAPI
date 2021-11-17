from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship

from .database import Base


class Station(Base):
    __tablename__ = "station"

    id = Column(Integer, primary_key=True, index=True)
    type_of_station = Column(String, index=True)
    name = Column(String, index=True)

    weather = relationship("Weather", back_populates="station")


class Weather(Base):
    __tablename__ = "weather"

    id = Column(Integer, primary_key=True, index=True)
    temperature = Column(Float, index=True)
    pressure = Column(Float, index=True)
    humidity = Column(Float, index=True)
    timestamp = Column(DateTime, index=True)
    station_id = Column(Integer, ForeignKey('station.id'))

    station = relationship("Station", back_populates="weather")
