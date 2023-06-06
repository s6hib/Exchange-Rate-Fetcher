# Exchange Rate Fetcher

## Introduction

Exchange Rate Fetcher is a Python application that fetches and displays the current exchange rates for a given base currency. It leverages the Exchange Rates API to obtain real-time currency exchange data.

## Requirements

To run this application, you need:

- Python installed on your machine.
- `requests` Python library, which can be installed with `pip install requests`.

## How to Use

1. Save the script in a Python file named `main.py`.

2. Open a terminal/command prompt.

3. Navigate to the directory containing the script using the `cd` command.

4. Run the script with the command:

    ```
    python main.py
    ```

5. When prompted, enter the base currency (like USD, EUR, GBP, etc.).

The application will fetch and display the current exchange rates for the base currency.

## Extending the Project

This project can be extended in several ways to meet your specific needs or to practice your Python skills. For example:

- Add error handling to ensure the application doesn't crash if the API request fails.
- Allow the user to specify a second currency, and display the exchange rate between the base currency and the second currency.
- Implement a GUI using a library like Tkinter or PyQt.
- Store exchange rate data in a database or a file for future reference.
