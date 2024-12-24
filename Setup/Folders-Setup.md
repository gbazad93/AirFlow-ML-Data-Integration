# Setting Up Folders

This guide helps you verify and set up the necessary folders for your Airflow project.

---

## 1. Verify or Set Your `AIRFLOW_HOME`
Airflow uses the default directory `~/airflow` unless explicitly changed. Follow these steps to ensure the `AIRFLOW_HOME` environment variable is correctly set:

```bash
# Check the current AIRFLOW_HOME value
echo $AIRFLOW_HOME
# Example output: /home/youruser/airflow

# If not set or incorrect, set it temporarily for the current session:
export AIRFLOW_HOME=~/airflow

# Save the change permanently (adjust for your shell configuration file, e.g., .bashrc, .zshrc):
echo "export AIRFLOW_HOME=~/airflow" >> ~/.bashrc

# Reload the shell configuration to apply changes
source ~/.bashrc
```

## 2. Create the `dags` and `helpers` Folders

Set up the required folders for your Airflow project:

```bash
# Create the dags folder for storing DAG definitions
mkdir -p $AIRFLOW_HOME/dags

# Create the helpers folder for custom scripts and modules
mkdir -p $AIRFLOW_HOME/helpers
```
### Folder Descriptions

- **`$AIRFLOW_HOME/dags`**:  
  Airflow automatically scans this folder for Python files containing DAG definitions. Place your `.py` files here to make them visible in the Airflow UI.

- **`$AIRFLOW_HOME/helpers`**:  
  This folder is for custom Python scripts or modules, such as data-fetching or cleaning methods. These can be imported into your DAGs by referencing them appropriately in your code.

By creating these folders, you ensure that your project is organized and ready for development with Airflow.

