from config.logger import logger
from config.settings import PROJECT_NAME


def extract():
    logger.info("Extraction phase started")
    print("\n[1/3] Starting Extraction Phase...")
    
    # Member 2 code will be called here later
    
    print("Extraction Phase Completed")
    logger.info("Extraction phase completed")


def transform():
    logger.info("Transformation phase started")
    print("\n[2/3] Starting Transformation Phase...")
    
    # Member 3 code will be called here later
    
    print("Transformation Phase Completed")
    logger.info("Transformation phase completed")


def load():
    logger.info("Loading phase started")
    print("\n[3/3] Starting Loading Phase...")
    
    # Member 4 code will be called here later
    
    print("Loading Phase Completed")
    logger.info("Loading phase completed")


def main():
    logger.info("ETL Pipeline Started")

    print("=" * 60)
    print(f"        {PROJECT_NAME}")
    print("=" * 60)

    extract()
    transform()
    load()

    print("\n" + "=" * 60)
    print("ETL PIPELINE COMPLETED SUCCESSFULLY")
    print("=" * 60)

    logger.info("ETL Pipeline Completed Successfully")


if __name__ == "__main__":
    main()