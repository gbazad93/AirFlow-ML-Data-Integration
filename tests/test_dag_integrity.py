"""Integrity checks for the weather_data_pipeline DAG.

These tests never call the OpenWeather API or PostgreSQL. They only assert that
the DAG file parses, that the expected tasks exist and that the dependency order
matches the one documented in the README.
"""

import os

import pytest
from airflow.models import DagBag

DAGS_FOLDER = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "dags",
)

EXPECTED_TASKS = {"load_locations", "fetch_weather_data", "insert_weather_data"}


@pytest.fixture(scope="module")
def dagbag():
    return DagBag(dag_folder=DAGS_FOLDER, include_examples=False)


def test_no_import_errors(dagbag):
    """A syntax or import error in any DAG file should fail the build."""
    assert not dagbag.import_errors, f"DAG import errors: {dagbag.import_errors}"


def test_pipeline_dag_is_loaded(dagbag):
    assert "weather_data_pipeline" in dagbag.dags


def test_expected_tasks_exist(dagbag):
    dag = dagbag.dags["weather_data_pipeline"]
    assert set(dag.task_ids) == EXPECTED_TASKS


def test_task_dependencies(dagbag):
    dag = dagbag.dags["weather_data_pipeline"]
    load = dag.get_task("load_locations")
    fetch = dag.get_task("fetch_weather_data")
    insert = dag.get_task("insert_weather_data")

    assert load.downstream_task_ids == {"fetch_weather_data"}
    assert fetch.downstream_task_ids == {"insert_weather_data"}
    assert insert.downstream_task_ids == set()


def test_locations_csv_is_present():
    """load_locations() reads dags/data/locations.csv at runtime."""
    csv_path = os.path.join(DAGS_FOLDER, "data", "locations.csv")
    assert os.path.isfile(csv_path)
