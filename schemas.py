from pydantic import BaseModel


class WeatherCreate(BaseModel):
    city: str
    temperature: float
    weather: str
