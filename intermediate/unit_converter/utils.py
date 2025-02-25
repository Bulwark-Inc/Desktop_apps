from collections import deque
from fractions import Fraction
import tkinter as tk

def validate_number(value):
    """Ensures the input is a valid number, supporting fractions and scientific notation."""
    try:
        if '/' in value:  # Handle fractions like "1/2"
            return float(Fraction(value))
        return float(value)  # Handle normal numbers and scientific notation
    except ValueError:
        return None

# Store last 5 conversions
recent_conversions = deque(maxlen=5)

def add_to_history(conversion):
    """Adds a conversion record to history."""
    recent_conversions.append(conversion)

def get_recent_conversions():
    """Returns the last 5 conversions."""
    return list(recent_conversions)

def show_tooltip(widget, text):
    """Displays a tooltip for a given widget."""
    tooltip = tk.Toplevel(widget)
    tooltip.wm_overrideredirect(True)
    tooltip.geometry(f"+{widget.winfo_rootx()}+{widget.winfo_rooty() + 30}")
    label = tk.Label(tooltip, text=text, background="yellow", relief="solid", borderwidth=1)
    label.pack()
    widget.tooltip = tooltip

def hide_tooltip(widget):
    """Hides the tooltip."""
    if hasattr(widget, "tooltip"):
        widget.tooltip.destroy()
        del widget.tooltip

def handle_keyboard_shortcut(event, convert_func, clear_func):
    """Handles keyboard shortcuts: Enter for conversion, Esc to clear."""
    if event.keysym == "Return":
        convert_func()
    elif event.keysym == "Escape":
        clear_func()
