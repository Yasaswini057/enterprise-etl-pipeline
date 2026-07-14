import pandas as pd
import os


def clean_customers(input_file, output_file):
    """Convert raw customer JSON into the established processed CSV schema."""

    df = pd.read_json(input_file)

    processed = pd.DataFrame()

    processed["customer_id"] = df["id"].apply(
        lambda x: f"C{x:03d}"
    )

    processed["first_name"] = df["name"].apply(
        lambda x: x.split()[0]
    )

    processed["last_name"] = df["name"].apply(
        lambda x: " ".join(x.split()[1:])
    )

    processed["email"] = df["email"]

    processed["phone"] = df["phone"]

    processed["city"] = df["address"].apply(
        lambda x: x["city"]
    )

    processed["registration_date"] = pd.Timestamp.today().normalize()

    os.makedirs("data/processed", exist_ok=True)

    processed.to_csv(output_file, index=False)

    print(f"Customers processed : {len(processed)}")
