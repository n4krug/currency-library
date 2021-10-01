import requests


class CurrencyConverter:
    def __init__(self, app_id):
        self.app_id = app_id

    # Get latest currency data from openexchangerates
    def get_rates(self, base="USD"):

        params = {"app_id": self.app_id, "base": base}

        currencies = requests.get(
            f"https://openexchangerates.org/api/latest.json", params
        ).json()

        rates = currencies["rates"]

        return rates

    def convert_currencies(
        self, rates, in_amount, in_currency="USD", out_currency="EUR"
    ):
        USD_amount = round(in_amount / rates[in_currency], 2)

        out_amount = round(USD_amount * rates[out_currency], 2)

        return out_amount
