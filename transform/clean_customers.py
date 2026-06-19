import pandas as pd

def clean_customers(input_file, output_file):
    # Load JSON data
    df = pd.read_json(input_file)

    # Remove duplicate records
    df = df.drop_duplicates()

    # Handle missing values
    df = df.fillna("Unknown")

    # Standardize text columns
    df["first_name"] = df["first_name"].str.title()
    df["last_name"] = df["last_name"].str.title()
    df["city"] = df["city"].str.title()

    # Convert registration date
    df["registration_date"] = pd.to_datetime(
        df["registration_date"]
    )

    # Save processed file
    df.to_csv(output_file, index=False)

    print(f"Customers processed: {output_file}")