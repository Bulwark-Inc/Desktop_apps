import tkinter as tk
from ttkbootstrap import Style
from logic import TimeZoneConverter  # Import logic class
import pytz
from utils import AutoCompleteCombobox, get_all_timezones  # Import custom combobox

time_zones = get_all_timezones()

class TimeConverterUI:
    """GUI for the Time Converter app using ttkbootstrap."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Time Zone Converter")
        self.root.geometry("400x300")

        # Apply a modern theme
        self.style = Style(theme="darkly")  # Change theme as needed

        # Create logic handler
        self.converter = TimeZoneConverter()

        # Widgets
        self.create_widgets()

    def create_widgets(self):
        """Create UI components."""
        # Time Input
        tk.Label(self.root, text="Enter Time:", font=("Arial", 12)).pack(pady=5)
        self.time_entry = tk.Entry(self.root, font=("Arial", 12))
        self.time_entry.pack(pady=5)

        # Source Timezone Dropdown
        tk.Label(self.root, text="From Timezone:", font=("Arial", 12)).pack(pady=5)
        self.source_tz = AutoCompleteCombobox(self.root)
        self.source_tz.set_completion_list(pytz.all_timezones)
        self.source_tz.pack(pady=5)

        # Target Timezone Dropdown
        tk.Label(self.root, text="To Timezone:", font=("Arial", 12)).pack(pady=5)
        self.target_tz = AutoCompleteCombobox(self.root)
        self.target_tz.set_completion_list(time_zones)
        self.target_tz.pack(pady=5)

        # Convert Button
        self.convert_button = tk.Button(self.root, text="Convert", command=self.convert_time)
        self.convert_button.pack(pady=10)

        # Result Label
        self.result_label = tk.Label(self.root, text="", font=("Arial", 12), fg="yellow")
        self.result_label.pack(pady=5)

    def convert_time(self):
        """Handles the conversion when the button is clicked."""
        time_str = self.time_entry.get()
        source_tz = self.source_tz.get()
        target_tz = self.target_tz.get()

        result = self.converter.convert_time(time_str, source_tz, target_tz)
        self.result_label.config(text=result)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = TimeConverterUI(root)
    root.mainloop()
