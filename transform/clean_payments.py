import pandas as pd

def clean_payments(input_file, output_file):
    # Load JSON data
    df = pd.read_json(input_file)

    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values
    df = df.fillna("Unknown")

    # Standardize payment method
    df["payment_method"] = df["payment_method"].str.title()

    # Standardize payment status
    df["payment_status"] = df["payment_status"].str.title()

    # Convert date column
    df["payment_date"] = pd.to_datetime(
        df["payment_date"]
    )

    # Save CSV
    df.to_csv(output_file, index=False)

    print(f"Payments processed: {output_file}")