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
┌─────────────────┐
│ OpenWeather API │
└──────┬──────────┘
       │ (Fetch JSON)
       v
┌───────────────────┐
│   Airflow DAG     │
│ (weather_pipeline)│
└──────┬────────────┘
       │ (Cleanup & Transform)
       v
┌─────────────────┐
│ DataProcessor   │
└──────┬──────────┘
       │ (Insert into DB)
       v
┌─────────────────┐
│ DatabaseEngine  │
└──────┬──────────┘
       │ (SQLAlchemy engine)
       v
┌─────────────────┐
│ PostgreSQL DB   │
└─────────────────┘

```
## Setup Instructions

To set up the project, please follow the instructions in the **Setup** folder in the following order listed below.

- **[Airflow Setup](./Setup/Airflow-Setup.md):**  
  Step-by-step instructions for installing and configuring Apache Airflow.

- **[Database Setup](./Setup/Database-Setup.md):**  
  Guide for setting up the PostgreSQL database, including creating schemas and tables.

- **[Folder Setup](./Setup/Folders-Setup.md):**  
  Instructions for verifying and setting up the required folder structure for your Airflow project.

- **[IDE Setup](./Setup/IDE-Setup.md):**  
  Guide for installing and configuring Visual Studio Code (or another IDE) for developing Airflow DAGs and helper scripts.

- **[Airflow Connection Setup](./Setup/Airflow-ConnectionSetup.md):**  
  Detailed steps for securely setting up database connections within Airflow.

- **[API Connection Setup](./Setup/API-Connection-Setup.md):**  
  Instructions for obtaining an OpenWeather API key and securely adding it as an Airflow connection.

## Project Structure

The repository is organized as follows:

```plaintext
AirFlow-ML-Data-Integration/
├── dags/                       # Airflow DAGs for ETL orchestration
├── data_processing/            # Scripts for cleaning and transforming data
├── database_engine/            # Database connection and query helpers
├── Setup/                      # Setup instructions (Airflow, database, etc.)
│   ├── Airflow-Setup.md        # Airflow setup steps
│   ├── Database-Setup.md       # Database setup steps
├── tests/                      # Unit tests for the pipeline
├── README.md                   # Main project readme
└── requirements.txt            # Python dependencies
```


## Contributing

Contributions are welcome and appreciated! To contribute to this project, please follow these steps:

1. **Fork the Repository:**
   Click the "Fork" button on the GitHub page of this repository to create a copy under your own account.

2. **Create a New Branch:**
   git checkout -b feature/your-feature-name
   Choose a clear, descriptive name for your branch that reflects the changes you’re making.

3. **Make Your Changes:**
   - Add or modify code, tests, or documentation as needed.
   - Ensure that your code adheres to the style and format defined by this project (PEP 8 for Python).
   - If you are adding new features, include tests or update existing tests to maintain coverage and confirm that your additions work as intended.

4. **Run Tests:**

   Example test command
   ```bash
   pytest tests/
   ```
   Make sure all tests pass and there are no regressions.

5. **Commit Your Changes:**
   ```bash
   git add .
   git commit -m "Add your commit message here"
   ```
   Write clear and concise commit messages that explain what your changes do.

6. **Push and Open a Pull Request:**
   ```bash
   git push origin feature/your-feature-name
   ```
   Go to your forked repository on GitHub and open a Pull Request (PR) against the main branch of this repository. Describe your changes, why they’re needed, and how to test them.

7. **Code Review and Feedback:**
   - Be open to feedback and make the requested changes where applicable.

8. **Merge:**
   Once your PR is approved, it will be merged into the main branch.

**Note:** If you’re unsure about any aspect of your contribution or would like to propose an idea before coding, feel free to open an issue first. Constructive discussion helps ensure we move in a direction that benefits the entire community.
