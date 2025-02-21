import tkinter as tk
from tkinter import ttk, messagebox
import pyperclip
from logic import PasswordGenerator

class PasswordApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x350")
        self.root.config(bg="#2C3E50")  # Dark theme

        # Title
        tk.Label(root, text="Password Generator", font=("Arial", 16, "bold"), fg="white", bg="#2C3E50").pack(pady=10)

        # Frame for inputs
        frame = tk.Frame(root, bg="#2C3E50")
        frame.pack(pady=10)

        # Password Length
        tk.Label(frame, text="Length:", fg="white", bg="#2C3E50", font=("Arial", 12)).grid(row=0, column=0, padx=5)
        self.length_entry = ttk.Entry(frame, width=5)
        self.length_entry.grid(row=0, column=1, padx=5)
        self.length_entry.insert(0, "12")  # Default length

        # Checkboxes for options
        self.use_upper = tk.BooleanVar(value=True)
        self.use_digits = tk.BooleanVar(value=True)
        self.use_symbols = tk.BooleanVar(value=True)

        ttk.Checkbutton(root, text="Include Uppercase", variable=self.use_upper).pack(anchor="w", padx=40)
        ttk.Checkbutton(root, text="Include Numbers", variable=self.use_digits).pack(anchor="w", padx=40)
        ttk.Checkbutton(root, text="Include Symbols", variable=self.use_symbols).pack(anchor="w", padx=40)

        # Generate Button
        generate_btn = tk.Button(root, text="Generate", font=("Arial", 12, "bold"), bg="#28A745", fg="white", command=self.generate_password)
        generate_btn.pack(pady=10)

        # Password Display
        self.password_entry = tk.Entry(root, font=("Arial", 14), width=25, justify="center", state="readonly")
        self.password_entry.pack(pady=10)

        # Copy Button
        copy_btn = tk.Button(root, text="Copy", font=("Arial", 12, "bold"), bg="#3498DB", fg="white", command=self.copy_password)
        copy_btn.pack()

    def generate_password(self):
        """Generates a password based on user options."""
        try:
            length = int(self.length_entry.get())
            if length < 4:
                messagebox.showwarning("Warning", "Password should be at least 4 characters!")
                return
            
            password = PasswordGenerator.generate(
                length=length,
                use_upper=self.use_upper.get(),
                use_digits=self.use_digits.get(),
                use_symbols=self.use_symbols.get()
            )

            self.password_entry.config(state="normal")
            self.password_entry.delete(0, tk.END)
            self.password_entry.insert(0, password)
            self.password_entry.config(state="readonly")
        
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid length!")

    def copy_password(self):
        """Copies the generated password to clipboard."""
        password = self.password_entry.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Copied", "Password copied to clipboard!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordApp(root)
    root.mainloop()
