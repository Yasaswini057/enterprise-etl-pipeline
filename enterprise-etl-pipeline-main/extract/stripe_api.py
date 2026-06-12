from extract.api_client import APIClient

client = APIClient()

def fetch_payments():
    url = "https://dummyjson.com/carts"

    data = client.get_data(url)

    return data