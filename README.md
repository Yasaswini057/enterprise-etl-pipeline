# Enterprise ETL Pipeline

## Overview

Enterprise ETL Pipeline is a Python-based data engineering project that extracts data from multiple APIs, transforms and cleans the data, and loads it into a PostgreSQL database using SQLAlchemy ORM.

This project demonstrates a complete Extract, Transform, Load (ETL) workflow commonly used in enterprise data engineering.

---

## Features

- Extracts data from multiple REST APIs
- Cleans and transforms raw JSON data
- Converts JSON to CSV
- Loads data into PostgreSQL
- Uses SQLAlchemy ORM
- Foreign key relationships
- Modular project structure
- Logging support
- Environment variables using `.env`
- Error handling
- Automatic table creation

---

## Technologies Used

- Python
- PostgreSQL
- SQLAlchemy
- Pandas
- Requests
- python-dotenv
- JSON
- CSV

---

## Project Workflow

```
Extract
   ↓
Transform
   ↓
Load
   ↓
PostgreSQL Database
```

---

## Data Sources

### Customers
https://jsonplaceholder.typicode.com/users

### Payments
https://dummyjson.com/carts

### Tickets
https://dummyjson.com/posts

---

## Database Tables

- Customers
- Tickets
- Payments

---

## Folder Structure

```
enterprise_etl_pipeline/

extract/
transform/
load/
config/
data/
logs/
reports/
main.py
requirements.txt
README.md
```

---

## How to Run

Clone the repository

```
git clone <repository-url>
```

Install dependencies

```
pip install -r requirements.txt
```

Configure `.env`

```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=etl_warehouse
DB_USER=postgres
DB_PASSWORD=your_password
```

Run the project

```
python main.py
```

---

## Sample Output

```
Customers Loaded : 10

Payments Loaded : 30

Tickets Loaded : 30

ETL PIPELINE COMPLETED SUCCESSFULLY
```

---

## Future Enhancements

- Apache Airflow Integration
- Docker Support
- AWS Deployment
- Power BI Dashboard
- Incremental Data Loading
- Data Validation Framework

---


Python Development Internship Project