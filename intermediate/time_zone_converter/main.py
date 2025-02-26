import tkinter as tk
from ui import TimeConverterUI

def main():
    """Main entry point for the Time Zone Converter App."""
    root = tk.Tk()
    app = TimeConverterUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
