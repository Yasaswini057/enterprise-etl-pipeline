from extract.api_client import APIClient

client = APIClient()


def fetch_customers():
    """Fetch customer records from the current Salesforce placeholder source."""
    # TODO: Replace the Salesforce dummy API with the approved REST API.
    url = "https://jsonplaceholder.typicode.com/users"
    return client.get_data(url)
