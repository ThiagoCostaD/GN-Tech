import logging
import os
from datetime import datetime, timezone

import requests
from fastapi import Depends, FastAPI
from requests.auth import HTTPBasicAuth
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


USERNAME = os.getenv("METEOMATICS_USERNAME", "default_user")
PASSWORD = os.getenv("METEOMATICS_PASSWORD", "default_password")
BASE_URL = os.getenv("METEOMATICS_BASE_URL", "https://api.meteomatics.com")


@app.get("/weather/{latitude}/{longitude}")
def get_weather(
    latitude: float,
    longitude: float,
    db: Session = Depends(get_db)
):

    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    parameters = "t_max_2m_24h:C"
    url = f"{BASE_URL}/{now}/{parameters}/{latitude},{longitude}/json"
    print(f"URL: {url}")

    logger.info(f"Request for {url} started.")

    response = requests.get(url, auth=HTTPBasicAuth(USERNAME, PASSWORD))

    if response.status_code != 200:
        logger.error(f"Meteomatics API error: {response.status_code}")
        return {
            "error": "Failed to retrieve weather data",
            "status_code": response.status_code
        }

    data = response.json()

    if "data" not in data or not data["data"]:
        logger.warning(f"No data available for {latitude}, {longitude}")
        return {"error": "No data available for this location"}

    try:
        temp = data["data"][0]["coordinates"][0]["dates"][0]["value"]
        logger.info(f"Received temperature: {temp}°C")

    except (KeyError, IndexError) as e:
        logger.error(f"Error processing API response: {e}")
        return {"error": "Error processing returned data"}

    weather_data = schemas.WeatherCreate(
        city=f"{latitude},{longitude}",
        temperature=temp,
        weather=f"Max temperature: {temp}°C"
    )

    logger.info(f"Storing data in database: {weather_data}")
    return crud.create_weather(db, weather_data)
