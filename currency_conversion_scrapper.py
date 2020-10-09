import requests
from bs4 import BeautifulSoup
from decimal import Decimal

# Takes in 2 Currencies and Returns the Exchange Rate as a Float (Done via Web Scrapping)
def find_conversion_rate(currency_from, currency_to):
	url = "https://transferwise.com/us/currency-converter/" + currency_from + "-to-" + currency_to + "-rate?amount=1"
	response = requests.get(url)
	soup = BeautifulSoup(response.text, "html.parser")
	conversion_rate = float(soup.find(class_="text-success").get_text())
	return conversion_rate

# Takes in the amount of currency and its exchange rate and returns the amount of the converted currency as a float
def convert_currency(amount, rate):
	return float(round(Decimal(str(amount * rate)), 2))
	# Uses 'Decimal' module to avoid rounding errors due to the nature of binary floating-point number

# Given the 2 currencies and amount of 1st currency, returns the converted amount of 2nd currency as a float
def find_converted_price(currency_from, currency_to, amount):
	rate = find_conversion_rate(currency_from, currency_to)
	return convert_currency(float(amount), rate)
