from gui import ConverterApp
import tkinter as tk

def main():
    """Main function to initialize the Number Converter app."""
    root = tk.Tk()
    app = ConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()