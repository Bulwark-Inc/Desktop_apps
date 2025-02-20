from api_handler import CurrencyAPI

class CurrencyConverter:
    """Handles currency conversion logic."""

    def __init__(self, api_key):
        self.api = CurrencyAPI(api_key)

    def convert(self, amount, source_currency, target_currency):
        """Converts the amount from one currency to another."""
        try:
            amount = float(amount)
            rate = self.api.get_exchange_rate(source_currency, target_currency)
            if isinstance(rate, str):  # Error message
                return rate
            return round(amount * rate, 2)
        except ValueError:
            return "Invalid amount. Please enter a number."

    def get_available_currencies(self):
        """Fetches available currencies from the API."""
        return self.api.get_available_currencies()
