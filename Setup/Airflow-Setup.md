# Setting Up Apache Airflow on Ubuntu

This guide provides step-by-step instructions to set up **Apache Airflow** on an Ubuntu. It includes system updates, Python installation, creating a virtual environment, installing Airflow, initializing the database, and starting the Airflow services.

---

## Prerequisites

- Ubuntu OS (tested on version 24.04).
- Basic familiarity with terminal commands.

---

## Steps to Set Up Apache Airflow

### Step 1: Update System Packages

```bash
# Update the package list and upgrade outdated packages
sudo apt update && sudo apt upgrade -y
```
### Step 2: Install Python and Required Tools

```bash
# Install Python and venv for managing virtual environments
sudo apt install -y python3 python3-venv

# Verify Python and pip installation
python3 --version
pip3 --version
```

### Step 3: Install `virtualenv`

```bash
# Install virtualenv
pip3 install virtualenv

# Create a virtual environment for Airflow
python3 -m venv ~/airflow_env

# Activate the virtual environment
source ~/airflow_env/bin/activate
```

### Step 4: Install Apache Airflow

```bash
# Set the AIRFLOW_HOME environment variable
export AIRFLOW_HOME=~/airflow

# Install Apache Airflow using pip
pip install apache-airflow
```

### Step 5: Initialize Airflow and Create a User

```bash
# Initialize the Airflow database
airflow db init

# Create an admin user for the Airflow Web UI
airflow users create \
    --username admin \
    --password admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com
```

### Step 6: Start Airflow

```bash
# Start the Airflow Scheduler (open a terminal)
airflow scheduler

# Start the Airflow Webserver (open another terminal)
airflow webserver --port 8080

# Access the Airflow Web UI at http://localhost:8080
```

## Notes

```bash
# To stop services, use CTRL+C.

# To reactivate the virtual environment after restarting the terminal:
source ~/airflow_env/bin/activate

# Ensure the AIRFLOW_HOME variable is set each time:
export AIRFLOW_HOME=~/airflow
```
---
### Disable Sample DAGs Without Deleting Files (Optional)

If you don’t want to see the example DAGs provided by Airflow, you can disable them:

1. Open the `airflow.cfg` configuration file. Typically, it is located in the `$AIRFLOW_HOME` directory:
   ```bash
   nano $AIRFLOW_HOME/airflow.cfg
   ```

2. Find the following line:
   ```text
   load_examples = True
   ```

3. Change it to:
   ```text
   load_examples = False
   ```

4. Save the file and exit.

5. Restart the Airflow services to apply the changes:
   ```bash
   airflow scheduler
   airflow webserver
   ```


