# Testing

What the test suite covers, and what it deliberately does not.

## What runs

The suite loads the DagBag and asserts that no file in the dags folder raised on import. That single assertion catches the failure mode that costs beginners the most time, because a syntax error or a missing provider package shows up in the UI as nothing at all rather than as an error.

Run it with `pytest tests -q` from the repository root, with the same environment the DAGs expect.

## What CI adds

The workflow runs three jobs in parallel. Ruff lints the dags and tests folders. A byte-compilation pass over the dags folder acts as a fast syntax gate, so an obvious typo fails in seconds rather than after a full Airflow install. The integrity tests then run against a constrained Airflow install.

The ordering matters: the cheap checks fail fast, so the slow job only runs on code that is at least syntactically sound.

## What is not covered

There are no tests that call the weather API or write to Postgres. That is intentional. Tests that need a live API key and a live database are not tests a contributor can run, and a tutorial repository is the wrong place to teach people to depend on network access in CI.

If you want that coverage, mock the hook rather than the HTTP layer. Asserting that the task calls insert_rows with the rows you expect is more useful than asserting that Postgres accepted them.

## Adding a test

Keep new tests import-safe and offline. If a test needs a connection, it belongs in a separate integration suite that is opt-in rather than part of the default run.
