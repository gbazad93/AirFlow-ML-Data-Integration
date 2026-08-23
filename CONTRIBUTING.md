# Contributing

Thanks for taking the time to contribute. This project is a teaching example, so small, focused and well-explained changes are especially welcome.

## Ways to help

- Report a bug or a broken setup step by opening an issue
- Improve the guides in the `Setup/` folder
- Add cities to `dags/data/locations.csv`
- Add transformations, tests or downstream machine learning examples

## Development setup

```bash
git clone https://github.com/gbazad93/AirFlow-ML-Data-Integration.git
cd AirFlow-ML-Data-Integration

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

## Before you open a pull request

```bash
ruff check dags tests
python -m compileall -q dags
pytest tests -q
```

All three commands also run automatically in CI on every pull request.

## Workflow

1. Fork the repository and create a branch: `git checkout -b feature/your-feature-name`
2. Make focused changes and keep the diff small
3. Follow PEP 8 and the formatting already used in `dags/ML_Data_ETL_dag.py`
4. Add or update tests when you change behaviour
5. Write a commit message that explains what changed and why
6. Open a pull request against `main` describing the change and how to test it

## Reporting bugs

Please include your Airflow version, Python version, the task that failed and the relevant part of the task log. Never paste your OpenWeather API key or database credentials into an issue.

## Code of Conduct

By participating in this project you agree to abide by the [Code of Conduct](./CODE_OF_CONDUCT.md).
