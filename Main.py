import tkinter as tk
from tkinter import ttk
import requests
def get_exchange_rates():
    api_key = '01af4fe0bc32c6271acb3ce9'  # Replace with your actual API key
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
    response = requests.get(url)
    data = response.json()
    return data['conversion_rates']
def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_var.get()
        to_currency = to_currency_var.get()
        rates = get_exchange_rates()
        
        if from_currency != 'USD':
            amount = amount / rates[from_currency]
        
        converted_amount = amount * rates[to_currency]
        result_label.config(text=f"{amount_entry.get()} {from_currency} = {converted_amount:.2f} {to_currency}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a numeric value.")
root = tk.Tk()
root.title("Currency Converter")

# Create and set variables
amount_var = tk.StringVar()
from_currency_var = tk.StringVar(value='USD')
to_currency_var = tk.StringVar(value='EUR')
amount_label = ttk.Label(root, text="Amount:")
amount_entry = ttk.Entry(root, textvariable=amount_var)

from_currency_label = ttk.Label(root, text="From Currency:")
from_currency_combobox = ttk.Combobox(root, textvariable=from_currency_var)
to_currency_label = ttk.Label(root, text="To Currency:")
to_currency_combobox = ttk.Combobox(root, textvariable=to_currency_var)

convert_button = ttk.Button(root, text="Convert", command=convert_currency)
result_label = ttk.Label(root, text="Result:")
rates = get_exchange_rates()
currency_list = list(rates.keys())

from_currency_combobox['values'] = currency_list
to_currency_combobox['values'] = currency_list
amount_label.grid(column=0, row=0, padx=5, pady=5)
amount_entry.grid(column=1, row=0, padx=5, pady=5)

from_currency_label.grid(column=0, row=1, padx=5, pady=5)
from_currency_combobox.grid(column=1, row=1, padx=5, pady=5)

to_currency_label.grid(column=0, row=2, padx=5, pady=5)
to_currency_combobox.grid(column=1, row=2, padx=5, pady=5)

convert_button.grid(column=0, row=3, columnspan=2, padx=5, pady=5)
result_label.grid(column=0, row=4, columnspan=2, padx=5, pady=5)
root.mainloop()

