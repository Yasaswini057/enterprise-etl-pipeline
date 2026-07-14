# Changelog

All notable documentation and maintainability updates for this project are
recorded here.

## Unreleased

### Improvements

- Added clear docstrings to the modified orchestration, API, transformation,
  loading, and visualization functions.
- Added concise TODO comments for planned production integrations and platform
  capabilities.
- Removed the unused `PROJECT_NAME` import from the pipeline entry point.
- Added opt-in Docker Compose support for the existing `python main.py` run.
- Added an isolated Docker-based Airflow deployment and an ETL DAG that calls
  the existing phase functions without duplicating their logic.

### Bug Fixes

- No runtime bug fixes were made; ETL behavior, APIs, generated files, database
  schema, loader behavior, and console output remain unchanged.

### Documentation Updates

- Rewrote the README with architecture, workflow, API-status, schema,
  installation, and operational guidance.
- Documented the current real Stripe integration and the Salesforce/Zendesk
  dummy integrations accurately.
- Added Docker and Airflow setup, access, and DAG-trigger instructions.

### Future Work

- Production Salesforce and Zendesk REST API integrations.
- Dashboard, CI/CD, monitoring, and data-quality enhancements.
