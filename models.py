from database import Base
from sqlalchemy import Column, Float, Integer, String


class WeatherData(Base):
    __tablename__ = "weather_data"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, index=True)
    temperature = Column(Float)
    weather = Column(String)
