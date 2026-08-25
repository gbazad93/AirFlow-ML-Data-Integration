# Changelog

Notable changes to this project. The format follows Keep a Changelog loosely; this is a tutorial repository rather than a released package, so there are no version tags yet.

## Unreleased

### Added

Docker Compose stack covering Airflow init, scheduler, webserver and PostgreSQL, so the example runs from a single command.

GitHub Actions CI with three parallel jobs: Ruff lint, byte-compilation of the dags folder as a fast syntax gate, and DAG integrity tests.

DAG integrity tests under tests/, which load the DagBag and assert there are no import errors.

Pinned requirements.txt, MIT LICENSE, and community health files including CONTRIBUTING, CODE_OF_CONDUCT and issue templates.

Security policy pointing reporters at the private advisory form.

Editor and git configuration to keep whitespace and line endings consistent.

### Changed

Weather inserts now batch through PostgresHook.insert_rows instead of opening a connection and committing once per city.

DAGs use the schedule argument rather than the deprecated schedule_interval, which was removed in Airflow 3.

### Fixed

Airflow artefacts and .env are now ignored, so local runs cannot commit airflow.db, airflow.cfg, logs or the OpenWeather key.
