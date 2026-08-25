# Airflow connections used by this project

The DAG does not hold any credentials itself. It looks up two Airflow connections at runtime, and both must exist before the first run or the tasks fail with a connection error.

## Postgres target

The destination for the cleaned weather rows. Docker Compose creates this pointing at the bundled Postgres service. For a local install, create it yourself with the host, port, schema, login and password of your own database.

Airflow encrypts the password field with its Fernet key, so the value never lives in the repository.

## Weather API

An HTTP connection whose host is the OpenWeather base URL. Store the API key in the password field or in the extra field, depending on how you prefer to build the request. Do not put it in the DAG file, and do not log the full request URL, because task logs are plain text and usually shipped to remote storage.

## Creating them

Either use Admin then Connections in the web UI, or the CLI with `airflow connections add`. The CLI form is the one worth keeping in your notes, because it is scriptable and gives you something to hand a new contributor.

List what already exists with `airflow connections list`. If a conn_id is missing, that is almost certainly why the DAG parsed fine but the task failed.

## In production

Swap the metadata database for a secrets backend rather than storing connections in Airflow itself. The DAG code does not change; only the resolution path does. This is the main reason the example reads from connections instead of environment variables.
