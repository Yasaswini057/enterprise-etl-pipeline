import pandas as pd
import os
from datetime import datetime


def clean_payments(input_file, output_file):

    raw = pd.read_json(input_file)

    carts = raw["carts"]

    records = []

    for cart in carts:

        records.append({
            "payment_id": f"P{cart['id']:03d}",
            "customer_id": f"C{((cart['userId'] - 1) % 10) + 1:03d}",
            "ticket_id": f"T{cart['id']:03d}",
            "amount": cart["discountedTotal"],
            "payment_method": "Credit Card",
            "payment_status": "Success",
            "payment_date": datetime.today().date()
        })

    df = pd.DataFrame(records)

    os.makedirs("data/processed", exist_ok=True)

    df.to_csv(output_file, index=False)

    print(f"Payments processed : {len(df)}")