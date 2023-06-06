import requests


def get_exchange_rates(base_currency, amount):
  base_url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"

  response = requests.get(base_url)
  exchange_data = response.json()

  if response.status_code == 200:
    rates = exchange_data["rates"]

    print(f"Exchange rates for {amount} {base_currency}:")
    for currency, rate in rates.items():
      converted_amount = round(
        amount * rate, 2)  # calculate equivalent amount in this currency
      print(f"{currency}: {converted_amount}")
  else:
    print("Error fetching exchange rates")


# Prompt for base currency and amount
base_currency = input("Enter base currency: ")
amount = float(
  input("Enter amount in base currency: "))  # convert input string to float

get_exchange_rates(base_currency, amount)
