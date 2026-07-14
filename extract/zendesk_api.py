from extract.api_client import APIClient

client = APIClient()


def fetch_tickets():
    """Fetch ticket records from the current Zendesk placeholder source."""
    # TODO: Replace the Zendesk dummy API with the approved REST API.
    url = "https://dummyjson.com/posts"

    data = client.get_data(url)

    return data
