from extract.api_client import get_data

def run_extraction():
    print("Running Extraction Module")

    get_data("Salesforce")
    get_data("Stripe")
    get_data("Zendesk")

    print("Extraction Module Completed")