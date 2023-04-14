# Currency Converter

This is a web application that allows users to convert an amount from one currency to another using the CurrencyAPI. The
application uses the Gradio library to create a user-friendly interface, allowing users to input the amount, select the
currencies to convert from and to, and get the exchanged value.

## Getting Started

1. Register for an API key from the CurrencyAPI website.

   ```https://app.currencyapi.com/register```

2. Create a .env file in the project directory and add your API key as follows:

   ```API_KEY=YOUR_API_KEY```

3. Install the required packages:

   ```pip install -r requirements.txt```

4. Run the script main.py:
   
   ```python main.py```

5. Access the web application at http://localhost:7860 in your browser.


## How to Use

1. Enter the amount you want to convert in the "Amount" input field.

2. Select the currency you want to convert from in the "From Currency" dropdown menu.

3. Select the currency you want to convert to in the "To Currency" dropdown menu.

4. Click on the "Submit" button to get the exchanged value.

5. You can also try the application with different currencies by selecting from the dropdown menus.

Note: Please make sure to enter valid currencies and amount for accurate results.