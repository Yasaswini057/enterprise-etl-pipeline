# Enterprise ETL Pipeline

## Project Overview
This project extracts data from multiple sources, transforms and cleans the data, and loads it into a centralized database.

## ETL Workflow

Salesforce / Stripe / Zendesk
          ↓
      Extract
          ↓
     Transform
          ↓
        Load
          ↓
   SQLite Database

## Technologies Used
- Python language
- Apache Airflow
- SQLite
- GitHub

## Project Structure
- extract/      -> Extraction Module
- transform/    -> Transformation Module
- load/         -> Loading Module
- airflow/      -> DAG Workflow
- docs/         -> Documentation
- logs/         -> Log Files

## Team Members


Member 1 - Integration & Airflow
Member 2 - Extraction
Member 3 - Transformation
Member 4 - Database
Member 5 - Testing & Documentation

## Project Flow

Extract → Transform → Load

## Technologies

Python
Pandas
PostgreSQL
SQLAlchemy
Airflow
Docker
GitHub

## Project Workflow

1. Extract data from APIs
2. Transform and clean data
3. Load data into PostgreSQL
4. Generate reports and dashboards

## Folder Structure

config/
extract/
transform/
load/
tests/
airflow/
docs/
docker/
requirements/

---

## Daily Progress Log

### Day 5 – Member 3 (Data Transformation)

#### Tasks Completed
- Pulled latest repository updates and synchronized local branch.
- Reviewed raw JSON datasets provided by the Data Extraction module.
- Implemented customer data transformation logic in `clean_customers.py`.
- Implemented payment data transformation logic in `clean_payments.py`.
- Implemented ticket data transformation logic in `clean_tickets.py`.
- Developed transformation workflow in `transformer.py`.
- Added data cleaning operations:
  - Duplicate record removal
  - Missing value handling
  - Text standardization
  - Date format conversion
- Generated processed CSV outputs from raw JSON data.
- Verified successful execution of the transformation pipeline.

#### Output Files Generated
- `data/processed/customers.csv`
- `data/processed/payments.csv`
- `data/processed/tickets.csv`

#### Current Status
Data Transformation module completed and integrated with the ETL workflow. Processed datasets are ready for the Database & Loading module.

#### Next Steps
- Support integration testing with Member 4 (Database & Loading).
- Verify processed data compatibility with PostgreSQL schema.
- Assist in end-to-end ETL pipeline testing.

- Member 1: Team Lead, Airflow, Integration
- Member 2: Extraction
- Member 3: Transformation
- Member 4: Loading & Database
- Member 5: Testing & Documentation

