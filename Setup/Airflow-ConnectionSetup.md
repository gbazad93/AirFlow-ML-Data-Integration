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

### Create a Database Connection in the Airflow UI

1. **Access the Airflow UI**:  
   Open your browser and navigate to the Airflow UI (e.g., `http://localhost:8080`).

2. **Log In**:  
   Use your Airflow admin credentials to log in.

3. **Navigate to Connections**:  
   Go to **Admin → Connections**.

4. **Create a New Connection**:  
   Click the plus (+) button to create a new connection.

5. **Install Postgres Provider (if needed)**:  
   If you do not see "Postgres" in the `Conn Type` dropdown, install the Postgres provider package:
   ```bash
   pip install apache-airflow-providers-postgres
   ```
Then restart both the scheduler and the webserver, and retry creating the connection.

6. **Fill Out the Connection Details**:  
   Enter the following information:
   - **Conn Id**: A descriptive name (e.g., `postgres_weather_db`).
   - **Conn Type**: Select `Postgres` (if using PostgreSQL).
   - **Host**: Enter your database host (e.g., `localhost` or a server hostname).
   - **Schema**: Enter your database name (e.g., `weather_data`).
   - **Login**: Enter your database user (e.g., `airflow_user`).
   - **Password**: Enter your database user’s password (e.g., `secure_password`).
   - **Port**: Typically `5432` for PostgreSQL.

7. **Save the Connection**:  
   Click **Save** to securely store the connection in Airflow.

---

## Referencing the Connection in DAGs

In the DAG code for this project, the database connection we just created is referenced using the exact **Conn Id** (`postgres_weather_db`) defined during the setup. This allows the DAG to securely interact with the database without hardcoding credentials directly in the code.

