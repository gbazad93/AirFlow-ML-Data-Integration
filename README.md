# AirFlow-ML-Data-Integration

This project demonstrates how to use [Apache Airflow](https://airflow.apache.org/) for orchestrating a daily ETL pipeline that fetches weather data from the free OpenWeather API, cleans and transforms the data, and stores it in a PostgreSQL database. It provides a scalable and reproducible example that can be extended for machine learning tasks such as training predictive models on weather-related datasets.


## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Setup Instructions](#setup-instructions)
- [Project Structure](#project-structure)
- [Airflow DAGs](#airflow-dags)
- [Database Engine](#database-engine)
- [Data Processing Helpers](#data-processing-helpers)
- [Extending the Pipeline](#extending-the-pipeline)
- [Contributing](#contributing)

## Overview
This repository offers a sample Airflow project integrating a daily weather data fetch from OpenWeather’s free API into a PostgreSQL database. The data is cleaned, validated, and ready for further downstream tasks, such as ML model training or dashboard visualization.

## Features
- **Automated Orchestration:** Daily scheduled runs controlled by Airflow.
- **Data Cleaning & Validation:** Ensures consistent, reliable data for analysis.
- **Modular Design:** Separate files for DAGs, database connection, and data processing.
- **Easily Extensible:** Add more cities, transformations, or ML tasks as needed.

## Architecture
```plaintext
         ┌─────────────────┐        ┌─────────────────┐
         │                 │        │                 │
         │ OpenWeather API │        │   Airflow DAG   │
         │                 │        │ (weather_pipeline)
         └───────┬────────┘        │                 │
                 │ (Fetch JSON)     └───────┬────────┘
                 │ (Cleanup & Transform)     │
                 v                           │ (Insert into)
         ┌─────────────────┐       ┌────────v────────┐
         │                 │       │                 │
         │ PostgreSQL DB   │<──────┤ DatabaseEngine  │
         │                 │       │                 │
         └─────────────────┘       └─────────────────┘
