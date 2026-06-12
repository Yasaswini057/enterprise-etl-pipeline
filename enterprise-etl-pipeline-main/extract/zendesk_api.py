from extract.api_client import APIClient

client = APIClient()

def fetch_tickets():
    url = "https://dummyjson.com/posts"

    data = client.get_data(url)

    return data