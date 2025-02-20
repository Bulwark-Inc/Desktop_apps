import requests

class CurrencyAPI:
    """Handles API requests to Fixer.io."""

    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://data.fixer.io/api"

    def get_exchange_rate(self, source_currency, target_currency):
        """Fetches exchange rate from Fixer.io API."""
        url = f"{self.base_url}/latest?access_key={self.api_key}"
        try:
            response = requests.get(url)
            data = response.json()

            if not data.get("success"):
                return f"API Error: {data.get('error', {}).get('info', 'Unknown error')}"

            rates = data.get("rates", {})
            if source_currency not in rates or target_currency not in rates:
                return "Invalid currency code."

            return rates[target_currency] / rates[source_currency]
        except requests.exceptions.RequestException:
            return "Network error. Please check your connection."

    def get_available_currencies(self):
        """Fetches the list of available currencies."""
        url = f"{self.base_url}/symbols?access_key={self.api_key}"
        try:
            response = requests.get(url)
            data = response.json()

            if not data.get("success"):
                return []

            return list(data.get("symbols", {}).keys())
        except requests.exceptions.RequestException:
            return []
