# Security Policy

## Supported versions

This is a tutorial project, so only the current `main` branch receives fixes.

## Reporting a vulnerability

Please do not open a public issue for a security problem. Use the private "Report a vulnerability" form under the Security tab of this repository, or contact the maintainer through the email on the GitHub profile. Expect an acknowledgement within seven days.

## Scope

The most likely issue in a project like this one is a leaked credential. The DAG reads its OpenWeather key from an Airflow connection or from a local `.env` file, and neither is committed. If you find a key anywhere in the history, please report it privately so it can be rotated before disclosure.
