# How the pipeline is put together

A short tour of the moving parts, for someone deciding whether to adapt this example rather than read it.

## Shape

Three stages, in the order you would expect. Extract pulls current conditions for a list of cities from the weather API. Transform normalises the response into flat rows and drops the fields the warehouse does not need. Load writes those rows to Postgres.

Each stage is a separate task, which means a failure in the API call does not leave you guessing whether anything was written.

## Why the load task looks the way it does

The obvious implementation loops over cities and issues one insert per city. It works, and it is slow in a way that gets worse linearly, because each iteration opens a connection and commits. The task now collects rows first and hands them to insert_rows with a commit interval, so the cost is roughly flat as the city list grows.

This is the one part of the example worth copying verbatim into real work.

## Where the credentials live

Nowhere in the repository. The tasks resolve two Airflow connections at runtime. See the connections document for what they are and how to create them.

## What is deliberately simple

No dynamic task mapping, no custom operators, no sensors. Those are the right tools at scale and the wrong tools for a first read, because they hide the data flow behind Airflow machinery. Once the three stages make sense, mapping the extract step across cities is a small change.

## Where to go next

The natural extensions are backfilling historical data, adding a data quality check between transform and load, and moving the metadata database off SQLite so tasks stop running one at a time.
