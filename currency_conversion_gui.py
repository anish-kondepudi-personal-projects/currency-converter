from tkinter import *
from currency_conversion_scrapper import find_converted_price, find_conversion_rate
from decimal import Decimal
import requests

# Recalculates Converted Value on 2nd Currency and Displays on UI
def calculate():
	unrounded_amount_currency_2 = float(amount_currency_1.get()) * float(round(Decimal(find_conversion_rate(currency_from.get(), currency_to.get())), 2))
	rounded_amount_currency_2 = float(round(Decimal(unrounded_amount_currency_2), 2))
	amount_currency_2.delete(0, END)
	amount_currency_2.insert(0, rounded_amount_currency_2)
	explanation.config(text=f"1 {currency_from.get()} is equal to {str(float(round(Decimal(find_conversion_rate(currency_from.get(), currency_to.get())), 2)))} {currency_to.get()}.")

# Checks for Internet Connection (Necessary for Scrapping)
try:
	requests.get("https://www.google.com/") # Test to see if there is a secure internet connection
	internet = True
except:
	print("No Internet. Please Connect and Try Again!")
	internet = False

if internet:

	# Creates Window along with Title, Icon, and Window Size
	root = Tk()
	root.title("Currency Converter")
	root.iconbitmap("./metadata/dollar_icon.ico")
	root.geometry("308x110")


	# Creates Drop Down Menus
	# Creates Default Vaues of Dropdown Menu and Defines Items in Menu as Strings
	currency_from = StringVar()
	currency_from.set("USD")
	currency_to = StringVar()
	currency_to.set("CAD")
	# Defines List of All Currencies
	currencies = ['EUR', 'GBP', 'INR', 'USD', 'AED', 'AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CZK', 'DKK', 'EUR', 'GBP', 'HKD', 'HRK', 'HUF', 'INR', 'JPY', 'MYR', 'NOK', 'NZD', 'PLN', 'RON', 'SEK', 'SGD', 'TRY']
	# Creates 2 Drop Down Menus
	drop_menu_1 = OptionMenu(root, currency_from, *currencies)
	drop_menu_2 = OptionMenu(root, currency_to, *currencies)
	#Determines Location on Grid of Both Drop Down Menus
	drop_menu_1.grid(row=0, column=0)
	drop_menu_2.grid(row=1, column=0)


	# Creates the Entry Boxes for the Amount of Each Currency
	# Box for Currency 1
	amount_currency_1 = Entry(root, width=38)
	amount_currency_1.grid(row=0, column=1)
	amount_currency_1.insert(0, 1)
	# Box for Currency 2
	amount_currency_2 = Entry(root, width=38)
	amount_currency_2.grid(row=1, column=1)
	amount_currency_2.insert(0, find_converted_price(currency_from.get(), currency_to.get(), 1))

	# Creates Text Which Shows Conversion Rate
	explanation = Label(root, text=f"1 {currency_from.get()} is equal to {str(float(round(Decimal(find_conversion_rate(currency_from.get(), currency_to.get())), 2)))} {currency_to.get()}.")
	explanation.grid(row=3, column=0, columnspan=2)

	# Creates Button Which Updates Entry Fields to Account for New Data by Calling the 'Calculate' Function
	recalculate = Button(root, text="Calculate", command=calculate, padx=123)
	recalculate.grid(row=2, column=0, columnspan=2)

	root.mainloop()