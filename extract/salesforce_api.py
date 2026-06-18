from extract.api_client import APIClient

client = APIClient()

def fetch_customers():
    url = "https://jsonplaceholder.typicode.com/users"

    data = client.get_data(url)

    return data