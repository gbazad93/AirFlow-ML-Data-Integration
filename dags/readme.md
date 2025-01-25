# Weather Data Pipeline

This folder contains the `weather_data_pipeline` DAG, which automates the process of fetching weather data from the OpenWeather API and inserting it into a PostgreSQL database.

**Note**: Before running this pipeline, make sure you have followed the steps in the **[Setup Instructions](https://github.com/gbazad93/AirFlow-ML-Data-Integration/blob/main/README.md)** section to properly configure your environment, database, and API connections.

---

## Overview

The pipeline consists of the following steps:

1. **Load Locations**: Read a list of locations from a CSV file located in the `data` folder.
2. **Fetch Weather Data**: Use the OpenWeather API to fetch current weather data for the locations.
3. **Insert Weather Data**: Insert the collected weather data into a PostgreSQL database.

---

## How It Works

### Step 1: Load Locations

The `load_locations` task reads a list of cities, along with their latitude and longitude, from a CSV file located at `dags/data/locations.csv`. The file must have the following format:

```csv
city,lat,lon
Seattle,47.6062,-122.3321
Los Angeles,34.0522,-118.2437
Chicago,41.8781,-87.6298
```

---

### Step 2: Fetch Weather Data

The `fetch_weather_data` task retrieves weather data for the cities in the CSV using the OpenWeather API. The task uses an Airflow connection named **`openweather_api_key`** to securely access the API.

---

### Step 3: Insert Weather Data

The `insert_weather_data` task inserts the fetched weather data into the PostgreSQL database. This task requires a valid Airflow connection named **`postgres_weather_db`**.

---

## Folder Structure

- **`main/dags/`**: Contains DAG scripts for your Airflow pipelines.
- **`main/dags/data/`**: Contains the `locations.csv` file listing cities and their coordinates.

---

## How to Run

1. Place the `locations.csv` file in the `dags/data` folder. Ensure the file has the required format.
2. Trigger the `weather_data_pipeline` DAG from the Airflow web UI.
3. Verify that the weather data is successfully inserted into the `weather` table in your PostgreSQL database.

---

## Debugging

- **Check Airflow Logs**: For detailed error messages if any task fails.
- **Validate API Key**: Ensure that your API key is correct and valid by testing it outside Airflow using tools like `curl` or Python scripts.
- **Verify Database Credentials**: Ensure your database connection credentials and permissions in PostgreSQL are correct.

---

