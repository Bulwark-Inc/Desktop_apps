import tkinter as tk
from tkinter import ttk, messagebox
from logic import TemperatureConverter

class TemperatureConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Temperature Converter")
        self.root.geometry("400x300")
        self.root.configure(bg="#1e1e2e")
        
        # Title Label
        ttk.Label(root, text="Temperature Converter", font=("Arial", 16, "bold"), foreground="#00FF00", background="#1e1e2e").pack(pady=10)
        
        # Input Field
        self.value_entry = ttk.Entry(root, font=("Arial", 12))
        self.value_entry.pack(pady=10, padx=20, ipadx=5, ipady=5, fill=tk.X)
        
        # Dropdowns for units
        self.units = ["Celsius", "Fahrenheit", "Kelvin"]
        self.from_unit = ttk.Combobox(root, values=self.units, state="readonly", font=("Arial", 12))
        self.from_unit.set("Celsius")
        self.from_unit.pack(pady=5, padx=20, fill=tk.X)
        
        self.to_unit = ttk.Combobox(root, values=self.units, state="readonly", font=("Arial", 12))
        self.to_unit.set("Fahrenheit")
        self.to_unit.pack(pady=5, padx=20, fill=tk.X)
        
        # Convert Button
        self.convert_button = ttk.Button(root, text="Convert", command=self.convert_temperature, style="Tech.TButton")
        self.convert_button.pack(pady=15)
        
        # Result Label
        self.result_label = ttk.Label(root, text="", font=("Arial", 14, "bold"), foreground="#00FF00", background="#1e1e2e")
        self.result_label.pack(pady=10)
        
        # Style Configuration
        style = ttk.Style()
        style.configure("Tech.TButton", font=("Arial", 12, "bold"), background="#007BFF", foreground="blue", padding=10)
    
    def convert_temperature(self):
        try:
            value = self.value_entry.get()
            converter = TemperatureConverter(value, self.from_unit.get(), self.to_unit.get())
            result = converter.convert()
            self.result_label.config(text=f"{value} {self.from_unit.get()} = {result} {self.to_unit.get()}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureConverterApp(root)
    root.mainloop()
