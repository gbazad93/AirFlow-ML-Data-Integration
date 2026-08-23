-- Runs automatically the first time the postgres container starts.
-- Creates the weather database and the table written to by insert_weather_data.

CREATE DATABASE weather;

\connect weather

CREATE TABLE IF NOT EXISTS weather (
    id SERIAL PRIMARY KEY,
    city VARCHAR(100) NOT NULL,
    date DATE NOT NULL,
    temperature NUMERIC(6, 2),
    humidity INTEGER,
    wind_speed NUMERIC(6, 2),
    weather_condition VARCHAR(150)
);

CREATE INDEX IF NOT EXISTS idx_weather_city_date ON weather (city, date);
