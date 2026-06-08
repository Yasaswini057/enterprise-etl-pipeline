def extract():
    print("Starting Extraction Phase")

def transform():
    print("Starting Transformation Phase")

def load():
    print("Starting Loading Phase")

def main():
    print("=" * 40)
    print("Enterprise ETL Pipeline Started")
    print("=" * 40)

    extract()
    transform()
    load()

    print("=" * 40)
    print("Pipeline Completed Successfully")
    print("=" * 40)

if __name__ == "__main__":
    main()