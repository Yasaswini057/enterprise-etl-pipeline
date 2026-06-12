import requests

class APIClient:
    def get_data(self, url, headers=None):
        try:
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()
            return response.json()

        except Exception as e:
            print(f"API Error: {e}")
            return None