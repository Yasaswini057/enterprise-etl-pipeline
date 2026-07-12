import os
import pandas as pd
from datetime import datetime


def clean_payments(input_file, output_file):

    df = pd.read_json(input_file)

    records = []

    for _, payment in df.iterrows():

        records.append({

            "payment_id": payment["payment_id"],

            "customer_id": "C001",

            "ticket_id": "T001",

            "amount": payment["amount"],

            "payment_method": "Card",

            "payment_status": payment["status"],

            "payment_date": datetime.today().date()

        })

    payments = pd.DataFrame(records)

    os.makedirs("data/processed", exist_ok=True)

    payments.to_csv(output_file, index=False)

    print(f"Payments processed : {len(payments)}")