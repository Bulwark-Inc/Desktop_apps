from tkinter import Tk
from gui import CurrencyConverterApp

# Replace with your actual API key
API_KEY = "YOUR_API_KEY"

def main():
    """Main function to initialize the Currency Converter app."""
    root = Tk()
    app = CurrencyConverterApp(root, API_KEY)
    root.mainloop()

if __name__ == "__main__":
    main()
