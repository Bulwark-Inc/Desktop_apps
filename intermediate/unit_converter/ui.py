import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from converter import UnitConverter
from theme import apply_light_theme, apply_dark_theme
from utils import validate_number, show_tooltip, hide_tooltip, add_to_history, get_recent_conversions, handle_keyboard_shortcut
from collections import deque

class ConverterApp:
    """Graphical User Interface for the Unit Converter."""
    
    def __init__(self, master):
        self.master = master
        self.master.title("Unit Converter")
        self.master.geometry("400x450")

        self.recent_conversions = deque(maxlen=5)

        # Load sun and moon icons
        self.sun_icon = ImageTk.PhotoImage(Image.open("images/sun.png").resize((25, 25)))
        self.moon_icon = ImageTk.PhotoImage(Image.open("images/moon.png").resize((25, 25)))
        
        # Title Label
        self.label_title = tk.Label(master, text="Unit Converter", font=("Arial", 16, "bold"))
        self.label_title.pack(pady=10)

        # Theme toggle button
        self.is_light_mode = True
        self.theme_button = tk.Button(self.master, image=self.sun_icon, command=self.toggle_theme, bd=0, bg="white")
        self.theme_button.place(relx=0.98, rely=0.02, anchor="ne")  # Top-right position
       
        # Conversion category dropdown
        self.label_category = tk.Label(master, text="Select Category:")
        self.label_category.pack()
        self.category_var = tk.StringVar()
        self.category_dropdown = ttk.Combobox(master, textvariable=self.category_var, state="readonly")
        self.category_dropdown["values"] = ("Length", "Weight", "Volume", "Area", "Speed")
        self.category_dropdown.pack()
        self.category_dropdown.bind("<<ComboboxSelected>>", self.update_units)

        # Input field
        self.label_value = tk.Label(master, text="Enter Value:")
        self.label_value.pack()
        self.entry_value = tk.Entry(master)
        self.entry_value.pack()

        # Bind keyboard shortcuts
        self.entry_value.bind("<KeyPress>", lambda event: handle_keyboard_shortcut(event, self.perform_conversion, self.clear_fields))

        # Unit selection dropdowns
        self.label_from_unit = tk.Label(master, text="From:")
        self.label_from_unit.pack()
        self.from_unit_var = tk.StringVar()
        self.from_unit_dropdown = ttk.Combobox(master, textvariable=self.from_unit_var, state="readonly")
        self.from_unit_dropdown.pack()
        self.from_unit_dropdown.bind("<Enter>", lambda event: show_tooltip(self.from_unit_dropdown, "Select the unit to convert from"))
        self.from_unit_dropdown.bind("<Leave>", lambda event: hide_tooltip(self.from_unit_dropdown))

        self.label_to_unit = tk.Label(master, text="To:")
        self.label_to_unit.pack()
        self.to_unit_var = tk.StringVar()
        self.to_unit_dropdown = ttk.Combobox(master, textvariable=self.to_unit_var, state="readonly")
        self.to_unit_dropdown.pack()
        self.to_unit_dropdown.bind("<Enter>", lambda event: show_tooltip(self.to_unit_dropdown, "Select the unit to convert to"))
        self.to_unit_dropdown.bind("<Leave>", lambda event: hide_tooltip(self.to_unit_dropdown))

        # Convert Button
        self.convert_button = tk.Button(master, text="Convert", command=self.perform_conversion)
        self.convert_button.pack(pady=10)

        # Result Label
        self.label_result = tk.Label(master, text="Converted Value: -", font=("Arial", 12, "bold"))
        self.label_result.pack()

        # Recent Conversions
        self.label_recent = tk.Label(master, text="Recent Conversions:")
        self.label_recent.pack()
        self.listbox_recent = tk.Listbox(master, height=5, width=50)
        self.listbox_recent.pack()

        # Apply default theme
        apply_light_theme(self.master)
    
    def update_units(self, event=None):
        """Update available units based on selected category."""
        category = self.category_var.get()
        units = getattr(UnitConverter, f"{category.lower()}_factors", {}).keys()
        self.from_unit_dropdown["values"] = list(units)
        self.to_unit_dropdown["values"] = list(units)
        if units:
            self.from_unit_var.set(next(iter(units)))
            self.to_unit_var.set(next(iter(units)))
    
    def perform_conversion(self):
        """Handle conversion process."""
        value = validate_number(self.entry_value.get())
        if value is None:
            self.label_result.config(text="Invalid input!")
            return
        
        from_unit = self.from_unit_var.get()
        to_unit = self.to_unit_var.get()
        category = self.category_var.get()

        if not category or not from_unit or not to_unit:
            self.label_result.config(text="Error: Select all fields", fg="red")
            return

        result = UnitConverter.convert(value, from_unit, to_unit, category)
        self.label_result.config(text=f"Converted Value: {result}" if result else "Invalid Conversion", fg="green" if result else "red")
        add_to_history(f"{value} {from_unit} -> {result} {to_unit}")

        self.listbox_recent.delete(0, tk.END)
        for conv in get_recent_conversions():
            self.listbox_recent.insert(tk.END, conv)
    
    def clear_fields(self):
        """Clears all input fields."""
        self.entry_value.delete(0, tk.END)
        self.label_result.config(text="Converted Value: -", fg="black")
    
    def toggle_theme(self):
        """Switch between light and dark themes."""
        self.is_light_mode = not self.is_light_mode
        if self.is_light_mode:
            apply_light_theme(self.master)
            self.theme_button.config(image=self.sun_icon)
        else:
            apply_dark_theme(self.master)
            self.theme_button.config(image=self.moon_icon)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ConverterApp(root)
    root.mainloop()
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from converter import UnitConverter
from theme import apply_light_theme, apply_dark_theme
from utils import validate_number, show_tooltip, hide_tooltip, add_to_history, get_recent_conversions, handle_keyboard_shortcut
from collections import deque

class ConverterApp:
    """Graphical User Interface for the Unit Converter."""
    
    def __init__(self, master):
        self.master = master
        self.master.title("Unit Converter")
        self.master.geometry("400x450")

        self.recent_conversions = deque(maxlen=5)

        # Load sun and moon icons
        self.sun_icon = ImageTk.PhotoImage(Image.open("images/sun.png").resize((25, 25)))
        self.moon_icon = ImageTk.PhotoImage(Image.open("images/moon.png").resize((25, 25)))
        
        # Title Label
        self.label_title = tk.Label(master, text="Unit Converter", font=("Arial", 16, "bold"))
        self.label_title.pack(pady=10)

        # Theme toggle button
        self.is_light_mode = True
        self.theme_button = tk.Button(self.master, image=self.sun_icon, command=self.toggle_theme, bd=0, bg="white")
        self.theme_button.place(relx=0.98, rely=0.02, anchor="ne")  # Top-right position
       
        # Conversion category dropdown
        self.label_category = tk.Label(master, text="Select Category:")
        self.label_category.pack()
        self.category_var = tk.StringVar()
        self.category_dropdown = ttk.Combobox(master, textvariable=self.category_var, state="readonly")
        self.category_dropdown["values"] = ("Length", "Weight", "Volume", "Area", "Speed")
        self.category_dropdown.pack()
        self.category_dropdown.bind("<<ComboboxSelected>>", self.update_units)

        # Input field
        self.label_value = tk.Label(master, text="Enter Value:")
        self.label_value.pack()
        self.entry_value = tk.Entry(master)
        self.entry_value.pack()

        # Bind keyboard shortcuts
        self.entry_value.bind("<KeyPress>", lambda event: handle_keyboard_shortcut(event, self.perform_conversion, self.clear_fields))

        # Unit selection dropdowns
        self.label_from_unit = tk.Label(master, text="From:")
        self.label_from_unit.pack()
        self.from_unit_var = tk.StringVar()
        self.from_unit_dropdown = ttk.Combobox(master, textvariable=self.from_unit_var, state="readonly")
        self.from_unit_dropdown.pack()
        self.from_unit_dropdown.bind("<Enter>", lambda event: show_tooltip(self.from_unit_dropdown, "Select the unit to convert from"))
        self.from_unit_dropdown.bind("<Leave>", lambda event: hide_tooltip(self.from_unit_dropdown))

        self.label_to_unit = tk.Label(master, text="To:")
        self.label_to_unit.pack()
        self.to_unit_var = tk.StringVar()
        self.to_unit_dropdown = ttk.Combobox(master, textvariable=self.to_unit_var, state="readonly")
        self.to_unit_dropdown.pack()
        self.to_unit_dropdown.bind("<Enter>", lambda event: show_tooltip(self.to_unit_dropdown, "Select the unit to convert to"))
        self.to_unit_dropdown.bind("<Leave>", lambda event: hide_tooltip(self.to_unit_dropdown))

        # Convert Button
        self.convert_button = tk.Button(master, text="Convert", command=self.perform_conversion)
        self.convert_button.pack(pady=10)

        # Result Label
        self.label_result = tk.Label(master, text="Converted Value: -", font=("Arial", 12, "bold"))
        self.label_result.pack()

        # Recent Conversions
        self.label_recent = tk.Label(master, text="Recent Conversions:")
        self.label_recent.pack()
        self.listbox_recent = tk.Listbox(master, height=5, width=50)
        self.listbox_recent.pack()

        # Apply default theme
        apply_light_theme(self.master)
    
    def update_units(self, event=None):
        """Update available units based on selected category."""
        category = self.category_var.get()
        units = getattr(UnitConverter, f"{category.lower()}_factors", {}).keys()
        self.from_unit_dropdown["values"] = list(units)
        self.to_unit_dropdown["values"] = list(units)
        if units:
            self.from_unit_var.set(next(iter(units)))
            self.to_unit_var.set(next(iter(units)))
    
    def perform_conversion(self):
        """Handle conversion process."""
        value = validate_number(self.entry_value.get())
        if value is None:
            self.label_result.config(text="Invalid input!")
            return
        
        from_unit = self.from_unit_var.get()
        to_unit = self.to_unit_var.get()
        category = self.category_var.get()

        if not category or not from_unit or not to_unit:
            self.label_result.config(text="Error: Select all fields", fg="red")
            return

        result = UnitConverter.convert(value, from_unit, to_unit, category)
        self.label_result.config(text=f"Converted Value: {result}" if result else "Invalid Conversion", fg="green" if result else "red")
        add_to_history(f"{value} {from_unit} -> {result} {to_unit}")

        self.listbox_recent.delete(0, tk.END)
        for conv in get_recent_conversions():
            self.listbox_recent.insert(tk.END, conv)
    
    def clear_fields(self):
        """Clears all input fields."""
        self.entry_value.delete(0, tk.END)
        self.label_result.config(text="Converted Value: -", fg="black")
    
    def toggle_theme(self):
        """Switch between light and dark themes."""
        self.is_light_mode = not self.is_light_mode
        if self.is_light_mode:
            apply_light_theme(self.master)
            self.theme_button.config(image=self.sun_icon)
        else:
            apply_dark_theme(self.master)
            self.theme_button.config(image=self.moon_icon)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ConverterApp(root)
    root.mainloop()
