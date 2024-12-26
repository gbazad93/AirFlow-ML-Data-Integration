# Airflow Connection Setup

Efficiently managing your database credentials is critical for a secure and maintainable data pipeline. Airflow’s built-in Connections mechanism provides a secure way to store and manage these credentials outside your codebase. This guide outlines the steps to configure a database connection in Airflow, ensuring a streamlined and secure setup process.

---

## Steps to Set Up Your Database Connection in Airflow

### 1. Activate the Airflow Environment
Before running any Airflow commands, activate the virtual environment where Airflow is installed:

```bash
source ~/airflow_env/bin/activate
```

Once activated, your prompt should indicate that you are in the `(airflow_env)` environment.

---

### 2. Initialize and Start Airflow
#### Initialize the Airflow Database
If you haven’t initialized the Airflow database yet, run the following command:
```bash
airflow db init
```

#### Start the Scheduler
In one terminal, start the Airflow scheduler:
```bash
airflow scheduler
```

#### Start the Webserver
In another terminal, start the Airflow webserver:
```bash
airflow webserver -p 8080
```

You can now access the Airflow UI at [http://localhost:8080](http://localhost:8080).

---

### 3. Create a Database Connection in the Airflow UI
1. Open your browser and navigate to the Airflow UI (e.g., [http://localhost:8080](http://localhost:8080)).
2. Log in using your Airflow admin credentials.
3. Go to **Admin → Connections**.
4. Click the **plus (+)** button to create a new connection.
5. Fill out the connection details as follows:
   - **Conn Id**: A descriptive name (`postgres_weather_db`).
   - **Conn Type**: Select the database type (`Postgres` for PostgreSQL).
   - **Host**: Enter your database host (`localhost` or the actual host).
   - **Schema**: Enter your database name (`weather_data`).
   - **Login**: Enter your database user (`airflow_user`).
   - **Password**: Enter your database user’s password (e.g., `secure_password`).
   - **Port**: Default is `5432` for PostgreSQL.

6. Click **Save** to store the connection securely in Airflow.

---

## Referencing the Connection in DAGs

In the DAG code for this project, the database connection we just created is referenced using the exact **Conn Id** (`postgres_weather_db`) defined during the setup. This allows the DAG to securely interact with the database without hardcoding credentials directly in the code.

