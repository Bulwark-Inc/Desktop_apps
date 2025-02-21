import tkinter as tk
from tkinter import ttk, messagebox
from logic import NumberConverter

class ConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Number System Converter")
        self.root.geometry("450x450")
        self.root.config(bg="#1E2A38")  # Techy Dark Blue Background

        # Title Label
        title_label = tk.Label(root, text="Number System Converter", font=("Arial", 16, "bold"), fg="white", bg="#1E2A38")
        title_label.pack(pady=10)

        # Input Frame
        frame = tk.Frame(root, bg="#1E2A38")
        frame.pack(pady=10)

        # Input Field
        tk.Label(frame, text="Enter Number:", fg="white", bg="#1E2A38", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.input_field = tk.Entry(frame, font=("Arial", 12), width=20)
        self.input_field.grid(row=0, column=1, padx=5, pady=5)

        # Dropdown for Source System
        tk.Label(frame, text="From:", fg="white", bg="#1E2A38", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.number_system = ttk.Combobox(frame, values=["Decimal", "Binary", "Hexadecimal", "Octal"], state="readonly", font=("Arial", 12))
        self.number_system.grid(row=1, column=1, padx=5, pady=5)
        self.number_system.current(0)  # Default selection

        # Dropdown for Target System
        tk.Label(frame, text="To:", fg="white", bg="#1E2A38", font=("Arial", 12)).grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.target_system = ttk.Combobox(frame, values=["Decimal", "Binary", "Hexadecimal", "Octal"], state="readonly", font=("Arial", 12))
        self.target_system.grid(row=2, column=1, padx=5, pady=5)
        self.target_system.current(1)  # Default selection

        # Convert Button
        convert_btn = tk.Button(root, text="Convert", font=("Arial", 12, "bold"), bg="#28A745", fg="white", command=self.convert_number)
        convert_btn.pack(pady=10)

        # Result Display Area
        self.result_label = tk.Label(root, text="Result:", font=("Arial", 12, "bold"), fg="white", bg="#1E2A38")
        self.result_label.pack(pady=5)
        self.result_field = tk.Entry(root, font=("Arial", 12), width=30, bd=3, state="readonly")
        self.result_field.pack(pady=5)

        # Copy to Clipboard Button
        copy_btn = tk.Button(root, text="Copy to Clipboard", font=("Arial", 10), bg="#007BFF", fg="white", command=self.copy_to_clipboard)
        copy_btn.pack(pady=5)

    def convert_number(self):
        """Handles conversion based on user selection."""
        input_value = self.input_field.get()
        from_type = self.number_system.get()
        to_type = self.target_system.get()

        converter = NumberConverter()

        try:
            # Convert the input number
            if from_type == "Decimal":
                result = converter.decimal_to_other(input_value)
            elif from_type == "Binary":
                result = converter.binary_to_other(input_value)
            elif from_type == "Hexadecimal":
                result = converter.hexadecimal_to_other(input_value)
            elif from_type == "Octal":
                result = converter.octal_to_other(input_value)

            if isinstance(result, str):  # If error message
                messagebox.showerror("Conversion Error", result)
            else:
                result = result[to_type.lower()]
                self.result_field.config(state="normal")
                self.result_field.delete(0, tk.END)
                self.result_field.insert(0, result)
                self.result_field.config(state="readonly")
        
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def copy_to_clipboard(self):
        """Copies result to clipboard"""
        result = self.result_field.get()
        if result:
            self.root.clipboard_clear()
            self.root.clipboard_append(result)
            self.root.update()
            messagebox.showinfo("Copied!", "Result copied to clipboard.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ConverterApp(root)
    root.mainloop()
