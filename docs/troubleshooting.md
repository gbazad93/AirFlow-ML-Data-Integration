# Troubleshooting

The failures people hit most often when running this example, and what they usually mean.

## My DAG does not appear in the UI

Almost always an import error rather than Airflow failing to see the file. Run `airflow dags list-import-errors` to get the traceback. If the dag_id shows up in `airflow dags list` but not the UI, it is paused rather than missing. Confirm the folder Airflow is parsing with `airflow config get-value core dags_folder`.

## The load task fails with a connection error

The DAG expects a Postgres connection and an HTTP connection to already exist, with the conn_ids the DAG references. Docker Compose provisions them; a local install does not. Create them under Admin then Connections, or with `airflow connections add`.

## The API task returns 401

The OpenWeather key is missing or malformed. Keys are read from an Airflow connection or from `.env`. A common cause is quoting the value twice, which stores the quote characters as part of the key.

## The API task returns 429

Rate limiting on the free tier, which allows 60 calls per minute. If you extended the city list, either use the bulk endpoint, fan the calls out with dynamic task mapping, or add a retry with exponential backoff.

## Tasks run one at a time

Expected on SQLite, which forces the SequentialExecutor. Move the metadata database to Postgres to get real parallelism.

## Import errors after upgrading Airflow

Provider packages are versioned separately from Airflow itself. Install from `requirements.txt` together with the Airflow constraints file for your release, otherwise pip will resolve a provider version that does not match.

## Still stuck

Open a Q&A discussion with the output of `airflow dags list-import-errors` and the failing task log. Redact the API key first.
