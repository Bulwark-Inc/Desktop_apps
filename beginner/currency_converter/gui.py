import tkinter as tk
from tkinter import ttk, messagebox
from logic import CurrencyConverter

class CurrencyConverterApp:
    """Graphical User Interface for the Currency Converter."""

    def __init__(self, root, api_key):
        self.root = root
        self.root.title("Currency Converter")
        self.root.geometry("450x350")
        self.root.configure(bg="#f4f4f4")  # Light gray background
        self.converter = CurrencyConverter(api_key)

        # Fetch available currencies
        self.currencies = self.converter.get_available_currencies()
        if not self.currencies:
            messagebox.showerror("API Error", "Failed to load currency list.")
            root.destroy()
            return

        # Title Label
        tk.Label(root, text="Currency Converter", font=("Arial", 18, "bold"), bg="#f4f4f4").grid(row=0, column=0, columnspan=2, pady=15)

        # Amount Entry
        tk.Label(root, text="Amount:", font=("Arial", 12), bg="#f4f4f4").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.amount_entry = tk.Entry(root, font=("Arial", 12), width=15)
        self.amount_entry.grid(row=1, column=1, padx=10, pady=10)

        # Source Currency Dropdown
        tk.Label(root, text="From Currency:", font=("Arial", 12), bg="#f4f4f4").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.source_currency = ttk.Combobox(root, values=self.currencies, font=("Arial", 12), width=12, state="readonly")
        self.source_currency.grid(row=2, column=1, padx=10, pady=10)
        self.source_currency.current(0)  # Default to first currency

        # Target Currency Dropdown
        tk.Label(root, text="To Currency:", font=("Arial", 12), bg="#f4f4f4").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.target_currency = ttk.Combobox(root, values=self.currencies, font=("Arial", 12), width=12, state="readonly")
        self.target_currency.grid(row=3, column=1, padx=10, pady=10)
        self.target_currency.current(1)  # Default to second currency

        # Convert Button
        self.convert_button = tk.Button(root, text="Convert", font=("Arial", 14, "bold"), bg="#007BFF", fg="white", padx=10, pady=5, command=self.convert_currency)
        self.convert_button.grid(row=4, column=0, columnspan=2, pady=20)

        # Result Label
        self.result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#f4f4f4")
        self.result_label.grid(row=5, column=0, columnspan=2, pady=10)

    def convert_currency(self):
        """Handles the conversion when the button is clicked."""
        amount = self.amount_entry.get()
        source_currency = self.source_currency.get()
        target_currency = self.target_currency.get()

        if not amount:
            messagebox.showerror("Input Error", "Please enter an amount.")
            return

        result = self.converter.convert(amount, source_currency, target_currency)

        if isinstance(result, str):  # Error message
            messagebox.showerror("Conversion Error", result)
        else:
            self.result_label.config(text=f"{amount} {source_currency} = {result} {target_currency}")
