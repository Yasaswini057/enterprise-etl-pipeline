from extract.api_client import APIClient

client = APIClient()

def fetch_customers():
    url = "https://jsonplaceholder.typicode.com/users"
    return client.get_data(url)