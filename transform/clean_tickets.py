import os
import random
import pandas as pd
from datetime import datetime


def clean_tickets(input_file, output_file):
    """Convert raw ticket JSON into the established processed CSV schema."""

    raw = pd.read_json(input_file)

    posts = raw["posts"]

    records = []

    status_options = [
        "Open",
        "In Progress",
        "Resolved"
    ]

    priority_options = [
        "Low",
        "Medium",
        "High"
    ]

    for post in posts:

        records.append({

            "ticket_id": f"T{post['id']:03d}",

            # Maps API user to an existing customer
            "customer_id": f"C{((post['userId'] - 1) % 10) + 1:03d}",

            "issue_type": post["title"][:40],

            "description": post["body"],

            "status": random.choice(status_options),

            "priority": random.choice(priority_options),

            "created_date": datetime.today().date()

        })

    df = pd.DataFrame(records)

    os.makedirs("data/processed", exist_ok=True)

    df.to_csv(output_file, index=False)

    print(f"Tickets processed : {len(df)}")
