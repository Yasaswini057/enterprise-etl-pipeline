import pandas as pd

def clean_tickets(input_file, output_file):
    # Load JSON data
    df = pd.read_json(input_file)

    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values
    df = df.fillna("Unknown")

    # Standardize text fields
    df["status"] = df["status"].str.title()
    df["priority"] = df["priority"].str.title()
    df["issue_type"] = df["issue_type"].str.title()

    # Convert date
    df["created_date"] = pd.to_datetime(
        df["created_date"]
    )

    # Save CSV
    df.to_csv(output_file, index=False)

    print(f"Tickets processed: {output_file}")