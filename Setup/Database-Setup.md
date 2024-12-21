# Database Setup: PostgreSQL for Airflow Integration

PostgreSQL is a powerful, open-source, and feature-rich relational database management system. It is highly reliable and performs well for handling complex queries and large datasets, making it an excellent choice for data-intensive projects like orchestrating ETL pipelines in Apache Airflow.

### Why Use PostgreSQL?
- **Robustness:** Offers ACID compliance for reliable transactions.
- **Scalability:** Handles large volumes of data and high-concurrency workloads effectively.
- **Extensibility:** Supports custom functions, extensions (like PostGIS), and JSON for semi-structured data.
- **Cross-Platform:** Available on multiple operating systems with consistent functionality.

In this project, PostgreSQL is used to store weather data fetched and processed by Apache Airflow DAGs.

---

## Step 1: Install PostgreSQL
First, install PostgreSQL and its command-line tools:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y postgresql postgresql-contrib
```

### Step 2: Start and Enable PostgreSQL Service

```bash
# Start PostgreSQL service
sudo systemctl start postgresql

# Enable PostgreSQL to start on boot
sudo systemctl enable postgresql

# Check the status of the PostgreSQL service
sudo systemctl status postgresql
```
### Step 3: Access PostgreSQL CLI

```bash
# Switch to the postgres user
sudo -u postgres psql
```

### Step 4: Create the Database and User

Once inside the PostgreSQL CLI, run the following commands to create a database and a user for Airflow:

```sql
-- Create the weather_data database
CREATE DATABASE weather_data;

-- Create a user for Airflow with a secure password
CREATE USER airflow_user WITH PASSWORD 'your_password';

-- Grant all privileges on the weather_data database to the user
GRANT ALL PRIVILEGES ON DATABASE weather_data TO airflow_user;
```
### Step 5: Create the Weather Data Table

Switch to the `weather_data` database and create a table to store weather-related information. Run the following commands in the PostgreSQL CLI:

```sql
-- Connect to the weather_data database
\c weather_data

-- Create the weather table
CREATE TABLE IF NOT EXISTS weather (
    id SERIAL PRIMARY KEY,
    city VARCHAR(50),
    date DATE,
    temperature NUMERIC,
    humidity NUMERIC,
    wind_speed NUMERIC,
    weather_condition VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
This table is designed to store essential weather data, such as:

- **city**: The name of the city.
- **date**: The date of the weather record.
- **temperature**: The recorded temperature.
- **humidity**: The humidity percentage.
- **wind_speed**: The wind speed measurement.
- **weather_condition**: A brief description of the weather condition.
- **created_at**: The timestamp when the record was created (automatically populated).

To verify the table creation, you can run:
```sql
\d weather
```
## Notes

- The `weather_data` database stores weather-related information such as city, date, temperature, humidity, wind speed, and conditions. This data is ready for downstream tasks like machine learning model training or visualizations.
- Use strong passwords for database users to ensure security.
- The `created_at` column in the `weather` table automatically records the timestamp when a new row is added.
- When using the `\d weather` command in the PostgreSQL CLI, if the output ends with `(END)` and you cannot type, press **`q`** to exit the pager and return to the `psql` prompt.

