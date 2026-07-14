# Enterprise ETL Pipeline

## Project Overview

Enterprise ETL Pipeline is a modular Python application that extracts customer,
payment, and support-ticket data, transforms the raw records into CSV files, and
loads the processed data into PostgreSQL through SQLAlchemy ORM models. It is
designed as a practical enterprise ETL demonstration while retaining clear
separation between extraction, transformation, configuration, and loading.

## Enterprise ETL Architecture

```text
Salesforce dummy API   Stripe API   Zendesk dummy API
          \                |                /
                           v
                 data/raw/*.json
                           |
                           v
              transform/clean_*.py
                           |
                           v
              data/processed/*.csv
                           |
                           v
           load/loader.py + SQLAlchemy
                           |
                           v
                     PostgreSQL
```

## Folder Structure

```text
enterprise_etl_pipeline/
├── config/          # Settings, constants, and logging configuration
├── data/
│   ├── raw/         # Extracted JSON records
│   └── processed/   # Transformed CSV records
├── dags/            # Docker Airflow DAGs that orchestrate existing phases
├── airflow/         # Isolated Airflow image definition
├── extract/         # API clients and extraction orchestration
├── transform/       # Dataset-specific cleansing functions
├── load/            # SQLAlchemy database connection, models, and loader
├── tests/           # File and transformation availability checks
├── visualization/   # Optional database-record visualization
├── main.py          # ETL pipeline entry point
└── requirements.txt # Python dependencies
```

## Technologies Used

- Python
- PostgreSQL
- SQLAlchemy ORM
- Pandas
- Requests
- Stripe Python SDK
- python-dotenv
- JSON and CSV
- Pytest

## Features

- Modular Extract → Transform → Load workflow.
- Raw API responses persisted as JSON files.
- Cleaned datasets persisted as CSV files before loading.
- SQLAlchemy ORM models with customer-to-ticket and customer/ticket-to-payment
  foreign-key relationships.
- Upsert-style loading of existing records by primary key.
- Environment-based PostgreSQL and Stripe configuration.
- File-based application logging and phase-level console progress output.
- Optional record-count dashboard image generation.

## Current API Status

| Dataset | Current source | Status |
| --- | --- | --- |
| Customers | JSONPlaceholder, through `salesforce_api.py` | Dummy API integration |
| Payments | Stripe Payment Intents | Real API integration |
| Tickets | DummyJSON posts, through `zendesk_api.py` | Dummy API integration |

## Current Project Workflow

1. `main.py` displays the existing pipeline banner and starts extraction.
2. The extraction module fetches customers, payments, and tickets, then writes
   raw JSON into `data/raw/`.
3. The transformation module cleans each dataset and writes CSV files into
   `data/processed/`.
4. The loader reads the CSV files and inserts or updates PostgreSQL records.
5. The existing loading summary and completion output are displayed.

## Database Schema

| Table | Primary key | Key columns and relationships |
| --- | --- | --- |
| `customers` | `customer_id` | Name, email, phone, city, registration date |
| `tickets` | `ticket_id` | `customer_id` → `customers.customer_id`, issue details, status, priority |
| `payments` | `payment_id` | `customer_id` → `customers.customer_id`, `ticket_id` → `tickets.ticket_id`, amount and payment details |

## Installation

1. Clone the repository and open the project directory.
2. Create and activate a Python virtual environment (recommended).
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file with the required PostgreSQL and Stripe settings:

   ```env
   DB_HOST=localhost
   DB_PORT=5432
   DB_NAME=etl_warehouse
   DB_USER=postgres
   DB_PASSWORD=your_password
   STRIPE_SECRET_KEY=your_stripe_secret_key
   ```

## How to Run

Ensure PostgreSQL is available and the `.env` configuration is valid, then run:

```bash
python main.py
```

To validate Python syntax for the project:

```bash
python -m compileall .
```

## Docker

Docker support is opt-in and does not alter local execution. The `etl` service
runs the same `python main.py` command, while the `postgres` service provides a
containerized PostgreSQL database.

1. Copy `.env.example` to `.env` and provide a valid `STRIPE_SECRET_KEY`.
2. Start the PostgreSQL database and one ETL run:

   ```bash
   docker compose up --build etl
   ```

3. To run the ETL again after the database is running:

   ```bash
   docker compose run --rm etl
   ```

4. Stop services and retain database data:

   ```bash
   docker compose down
   ```

The database is persisted in the `etl-postgres-data` Docker volume. Use
`docker compose down -v` only when intentionally removing container database
data.

## Airflow with Docker

Airflow is deployed only through Docker; no native Windows Airflow installation
is required. The stack contains an Airflow webserver, scheduler, triggerer,
initialization service, metadata PostgreSQL database, and a separate ETL
PostgreSQL database.

1. Copy `.env.example` to `.env`, configure `STRIPE_SECRET_KEY`, and set a
   strong `AIRFLOW_ADMIN_PASSWORD`.
2. Generate an Airflow Fernet key and put it in `AIRFLOW_FERNET_KEY`:

   ```bash
   python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
   ```

3. Start the Airflow stack:

   ```bash
   docker compose -f docker-compose-airflow.yml up --build
   ```

4. Open <http://localhost:8080> and sign in with `AIRFLOW_ADMIN_USER` and
   `AIRFLOW_ADMIN_PASSWORD` from `.env`.
5. In the UI, enable `enterprise_etl_pipeline`, then select **Trigger DAG**.
   It executes the existing Extract → Transform → Load functions through three
   `PythonOperator` tasks.

To stop the Airflow stack while preserving volumes:

```bash
docker compose -f docker-compose-airflow.yml down
```

The legacy placeholder file under `airflow/dags/` remains untouched; the
Docker deployment uses the production DAG in `dags/etl_pipeline_dag.py`.

## Future Enhancements

- Replace the Salesforce dummy API with a production Salesforce REST API.
- Replace the Zendesk dummy API with a production Zendesk API.
- Add a production dashboard and reporting layer.
- Add CI/CD, automated integration tests, and data-quality validation.
