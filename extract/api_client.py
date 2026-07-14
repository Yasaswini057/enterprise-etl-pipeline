import requests

class APIClient:
    def get_data(self, url, headers=None):
        """Fetch and decode JSON data from an HTTP endpoint.

        Returns ``None`` when the existing request error handling intercepts an
        exception.
        """
        try:
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()
            return response.json()

        except Exception as e:
            print(f"API Error: {e}")
            return None
