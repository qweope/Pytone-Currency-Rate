from forex_python.converter import CurrencyRates


def get_rate(currency_from: str, currency_to: str) -> float:
    currency_rates = CurrencyRates()
    return currency_rates.get_rate(currency_from, currency_to)


if __name__ == "__main__":
    amount = float(input('Enter the amount:'))
    currency_from = str(input('Enter initial currency:')).strip().upper()
    currency_to = str(input('Enter desired currency:')).strip().upper()
    rate = get_rate(currency_from, currency_to)
    print(f'Converted {amount} {currency_from} with rate {rate} equals to {amount*rate} {currency_to}')
