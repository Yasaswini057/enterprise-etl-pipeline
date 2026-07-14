import os
import matplotlib.pyplot as plt
from load.database import engine
from sqlalchemy import text


def generate_dashboard():
    """Generate the existing database record-count dashboard image."""

    # TODO: Replace this static visualization with a production dashboard.

    os.makedirs("dashboard", exist_ok=True)

    with engine.connect() as conn:

        customers = conn.execute(
            text("SELECT COUNT(*) FROM customers")
        ).scalar()

        tickets = conn.execute(
            text("SELECT COUNT(*) FROM tickets")
        ).scalar()

        payments = conn.execute(
            text("SELECT COUNT(*) FROM payments")
        ).scalar()

    plt.figure(figsize=(8,6))

    labels = ["Customers", "Tickets", "Payments"]
    values = [customers, tickets, payments]

    colors = [
        "#3498db",
        "#2ecc71",
        "#f39c12"
    ]

    bars = plt.bar(
        labels,
        values,
        color=colors,
        edgecolor="black"
    )

    plt.title(
        "Enterprise ETL Pipeline",
        fontsize=18,
        fontweight="bold"
    )

    plt.ylabel("Records")

    for bar in bars:

        height = bar.get_height()

        plt.text(
            bar.get_x() + bar.get_width()/2,
            height + 0.5,
            str(int(height)),
            ha="center",
            fontsize=12,
            fontweight="bold"
        )

    plt.savefig("dashboard/records_loaded.png", dpi=300)

    plt.close()

    print("✓ Dashboard Created")

if __name__ == "__main__":
    print("Dashboard script started...")
    generate_dashboard()
    print("Dashboard script finished...")
