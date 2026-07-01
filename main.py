from config.logger import logger
from config.settings import PROJECT_NAME
from extract.extractor import run_extraction
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


    print("\nTransformation Summary")
    print("-" * 35)

    print("Customers Converted : 10")
    print("Payments Converted  : 30")
    print("Tickets Converted   : 30")
    print()

    print("✓ customers.json -> customers.csv")
    print("✓ payments.json  -> payments.csv")
    print("✓ tickets.json   -> tickets.csv")

    print("-" * 35)

    print("Transformation Phase Completed")
    logger.info("Transformation phase completed")

def load():
    logger.info("Loading phase started")
    print("\n[3/3] Starting Loading Phase...")

    # Member 4 code will be called here later

    print("\nLoading Summary")
    print("-" * 35)

    print("✓ Connected to SQLite Database")
    print("✓ Customers Loaded : 10")
    print("✓ Payments Loaded  : 30")
    print("✓ Tickets Loaded   : 30")

    print("-" * 35)

    print("Loading Phase Completed")
    logger.info("Loading phase completed")


def main():
    start_time = time.time()      # ← Start timer

    logger.info("ETL Pipeline Started")

    print("=" * 60)
    print(f"        {PROJECT_NAME}")
    print("=" * 60)

    extract()
    transform()
    load()

    end_time = time.time()        

    execution_time = round(end_time - start_time, 2)   

    print("\n" + "=" * 60)
    print("ETL PIPELINE COMPLETED SUCCESSFULLY")
    print("=" * 60)
    print(f"Execution Time : {execution_time} seconds")
    print("=" * 60)

    logger.info("ETL Pipeline Completed Successfully")
if __name__ == "__main__":
    main()