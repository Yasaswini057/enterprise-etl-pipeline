from config.logger import logger
from config.settings import PROJECT_NAME

from extract.extractor import run_extraction
from transform.transformer import run_transformations
from load.loader import run_loader

import time


def extract():

    logger.info("Extraction phase started")

    print("\n[1/3] Starting Extraction Phase...")

    run_extraction()

    print("Extraction Phase Completed")

    logger.info("Extraction phase completed")


def transform():

    logger.info("Transformation phase started")

    print("\n[2/3] Starting Transformation Phase...")

    run_transformations()

    print("Transformation Phase Completed")

    logger.info("Transformation phase completed")


def load():

    logger.info("Loading phase started")

    print("\n[3/3] Starting Loading Phase...")

    customers_loaded, payments_loaded, tickets_loaded = run_loader()

    total = customers_loaded + payments_loaded + tickets_loaded

    print("\nLoading Summary")
    print("-----------------------------------")
    print("✓ Connected to PostgreSQL Database")
    print(f"✓ Customers Loaded : {customers_loaded}")
    print(f"✓ Payments Loaded  : {payments_loaded}")
    print(f"✓ Tickets Loaded   : {tickets_loaded}")
    print("-----------------------------------")
    print(f"✓ Total Records Loaded : {total}")
    print("-----------------------------------")
    print("Loading Phase Completed")

    logger.info("Loading phase completed")


def main():

    start_time = time.time()

    logger.info("ETL Pipeline Started")

    print("=" * 65)
    print("           ENTERPRISE ETL PIPELINE")
    print("=" * 65)

    print("Data Sources")
    print(" ✓ Salesforce API")
    print(" ✓ Stripe API")
    print(" ✓ Zendesk API")

    print("\nDatabase")
    print(" ✓ PostgreSQL")

    print("\nWorkflow")
    print(" Extract")
    print("     ↓")
    print(" Transform")
    print("     ↓")
    print(" Load")

    print("=" * 65)

    try:

        extract()
        transform()
        load()

        execution_time = round(time.time() - start_time, 2)

        print("\n" + "=" * 60)
        print("ETL PIPELINE COMPLETED SUCCESSFULLY")
        print("=" * 60)
        print(f"Execution Time : {execution_time} seconds")
        print("=" * 60)

      

    except Exception as e:

        logger.exception(f"Pipeline Failed : {e}")

        print("\n" + "=" * 60)
        print("ETL PIPELINE FAILED")
        print("=" * 60)
        print(e)
        print("=" * 60)


if __name__ == "__main__":
    main()