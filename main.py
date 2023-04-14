import json
import os
import requests
from dotenv import load_dotenv
import gradio as gr
from gradio import components

def get_currencies() -> list:
    """
    Fetches the list of currencies from a JSON file and returns a sorted list of currency codes.

    Returns:
        list: List of currency codes
    """
    with open("currency.json", mode="r") as f:
        temp = []
        currency_data = json.load(f)
        for currency in currency_data:
            for code in currency:
                temp.append(code)
        return sorted(temp)


load_dotenv()

API_KEY = os.getenv("API_KEY")  # Load API key from environment variable
API_ENDPOINT = 'https://api.currencyapi.com/v3/latest'  # Endpoint for currency conversion API


def convert_currency(amount: float, from_currency: str, to_currency: str) -> float:
    """
    Converts an amount from one currency to another using the currency conversion API.

    Args:
        amount (float): Amount to be converted
        from_currency (str): Currency code of the original currency
        to_currency (str): Currency code of the target currency

    Returns:
        float: Converted amount in the target currency
    """
    query_params = {
        'apikey': API_KEY,
        'base_currency': from_currency,
        'currencies': to_currency
    }
    response = requests.get(API_ENDPOINT, params=query_params)
    currency_data = response.json()
    exchange_rate = currency_data['data'][to_currency]['value']
    exchanged_value = exchange_rate * amount
    return exchanged_value


currency_list = get_currencies()

# Define input components
amount_input = components.Number(label="Amount")
from_currency_input = components.Dropdown(choices=currency_list, label="From Currency")
to_currency_input = components.Dropdown(choices=currency_list, label="To Currency")

# Define output component
output = components.Textbox(label="Exchanged Value")


# Create Gradio interface
iface = gr.Interface(
    fn=convert_currency,
    inputs=[amount_input, from_currency_input, to_currency_input],
    outputs=output,
    title="Currency Converter",
    description="Converts an amount from one currency to another.",
)

# Run the Gradio app
iface.launch()
