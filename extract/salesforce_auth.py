import os
import requests
from dotenv import load_dotenv

load_dotenv()


def get_access_token():
    url = "https://login.salesforce.com/services/oauth2/token"

    payload = {
        "grant_type": "password",
        "client_id": os.getenv("SF_CLIENT_ID"),
        "client_secret": os.getenv("SF_CLIENT_SECRET"),
        "username": os.getenv("SF_USERNAME"),
        "password": os.getenv("SF_PASSWORD")
    }

    response = requests.post(url, data=payload)

    print("Status Code:", response.status_code)
    print("Response:", response.text)

    response.raise_for_status()

    data = response.json()

    return data["access_token"], data["instance_url"]