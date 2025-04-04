from sqlalchemy.orm import Session

import models
import schemas


def create_weather(db: Session, weather: schemas.WeatherCreate):
    db_weather = models.WeatherData(**weather.dict())
    db.add(db_weather)
    db.commit()
    db.refresh(db_weather)
    return db_weather


def get_weather_by_city(db: Session, city: str):
    return db.query(
        models.WeatherData
    ).filter(
        models.WeatherData.city == city
    ).all()


def get_all_weather(db: Session):
    return db.query(models.WeatherData).all()
