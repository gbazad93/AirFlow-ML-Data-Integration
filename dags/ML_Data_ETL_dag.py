import logging
import os
import json
import requests
import pandas as pd

from datetime import datetime, timedelta
from airflow import DAG
from airflow.hooks.base import BaseHook
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook

# Configure module-level logger
logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------
# Default DAG arguments
# ---------------------------------------------------------------------
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

# ---------------------------------------------------------------------
# DAG Definition
# ---------------------------------------------------------------------
with DAG(
    dag_id="weather_data_pipeline",
    default_args=default_args,
    description="Fetch weather data and insert into PostgreSQL",
    schedule_interval="0 23 * * *",
    start_date=datetime(2025, 01, 04),
    catchup=False,
) as dag:
    # -----------------------------------------------------------------
    # Step 1: Load Locations
    # -----------------------------------------------------------------
    def load_locations():
        """
        Load city locations from a CSV file and return as a JSON string.
        """
        file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "data",
            "locations.csv",
        )
        locations = pd.read_csv(file_path).to_dict(orient="records")
        return json.dumps(locations)

    load_locations_task = PythonOperator(
        task_id="load_locations",
        python_callable=load_locations,
    )

    # -----------------------------------------------------------------
    # Step 2: Fetch Weather Data
    # -----------------------------------------------------------------
    def fetch_weather_data(locations):
        """
        Fetch the current weather data for each location from the OpenWeather API.
        Returns the collected data as a JSON string.
        """
        connection = BaseHook.get_connection("openweather_api_key")
        api_key = connection.extra_dejson.get("api_key")

        # Parse the incoming locations string
        locations_list = json.loads(locations)
        base_url = connection.host
        weather_data = []

        for location_info in locations_list:
            lat, lon = location_info["lat"], location_info["lon"]
            city = location_info["city"]
            try:
                response = requests.get(
                    base_url,
                    params={"lat": lat, "lon": lon, "appid": api_key},
                    timeout=10,  # optional: set a timeout for requests
                )
                if response.status_code == 200:
                    data = response.json()
                    # Append weather record with an ISO-formatted date
                    weather_data.append(
                        {
                            "city": city,
                            "date": datetime.utcnow().date().isoformat(),
                            "temperature": data["main"]["temp"],
                            "humidity": data["main"]["humidity"],
                            "wind_speed": data["wind"]["speed"],
                            "weather_condition": data["weather"][0]["description"],
                        }
                    )
                else:
                    logger.error(
                        "Failed API call for %s (HTTP %s). Response: %s",
                        city,
                        response.status_code,
                        response.text,
                    )
            except Exception as exc:
                logger.error("Exception occurred for %s: %s", city, exc)

        return json.dumps(weather_data)

    fetch_weather_data_task = PythonOperator(
        task_id="fetch_weather_data",
        python_callable=fetch_weather_data,
        op_args=["{{ ti.xcom_pull(task_ids='load_locations') }}"],
    )

    # -----------------------------------------------------------------
    # Step 3: Insert Weather Data into PostgreSQL
    # -----------------------------------------------------------------
    def insert_weather_data(weather_data):
        """
        Insert the weather data (JSON string) into a PostgreSQL table.
        """
        # Convert JSON string to list of dicts
        if isinstance(weather_data, str):
            weather_data = json.loads(weather_data)

        # Convert ISO-formatted date strings to date objects
        for record in weather_data:
            record["date"] = datetime.fromisoformat(record["date"]).date()

        # Validate data format
        if not isinstance(weather_data, list) or not all(
            isinstance(record, dict) for record in weather_data
        ):
            raise ValueError(
                "Invalid format for weather_data; expected a list of dictionaries."
            )

        # Insert into PostgreSQL
        postgres_hook = PostgresHook(postgres_conn_id="postgres_weather_db")
        insert_query = """
            INSERT INTO weather (
                city,
                date,
                temperature,
                humidity,
                wind_speed,
                weather_condition
            ) VALUES (%s, %s, %s, %s, %s, %s)
        """

        for record in weather_data:
            postgres_hook.run(
                insert_query,
                parameters=(
                    record["city"],
                    record["date"],
                    record["temperature"],
                    record["humidity"],
                    record["wind_speed"],
                    record["weather_condition"],
                ),
            )

        logger.info("Weather data insertion completed.")

    insert_weather_data_task = PythonOperator(
        task_id="insert_weather_data",
        python_callable=insert_weather_data,
        op_args=["{{ ti.xcom_pull(task_ids='fetch_weather_data') }}"],
    )

    # -----------------------------------------------------------------
    # Task Dependencies
    # -----------------------------------------------------------------
    load_locations_task >> fetch_weather_data_task >> insert_weather_data_task
