import tkinter as tk
from tkinter import ttk

# Theme Colors
LIGHT_BG = "white"
LIGHT_FG = "black"
DARK_BG = "#2E2E2E"
DARK_FG = "white"
DARK_ENTRY_BG = "#4E4E4E"  # Darker shade for inputs

def apply_theme(root, theme="light"):
    """Applies a theme to the application."""
    bg_color = LIGHT_BG if theme == "light" else DARK_BG
    fg_color = LIGHT_FG if theme == "light" else DARK_FG
    entry_bg = LIGHT_BG if theme == "light" else DARK_ENTRY_BG  # Background for entry fields

    root.configure(bg=bg_color)

    # Configure ttk styles
    style = ttk.Style()
    style.configure("TLabel", background=bg_color, foreground=fg_color)
    style.configure("TButton", foreground=fg_color)

    # Explicitly configure Entry and Combobox fields for all states
    style.configure("TEntry", fieldbackground=entry_bg, foreground=fg_color, insertbackground=fg_color)
    style.configure("TCombobox", fieldbackground=entry_bg, foreground=fg_color, background=entry_bg)

    # Apply correct colors in readonly and disabled states
    style.map("TEntry",
              background=[("readonly", entry_bg), ("disabled", entry_bg)],
              foreground=[("readonly", fg_color), ("disabled", fg_color)]
              )

    style.map("TCombobox",
              fieldbackground=[("readonly", entry_bg)],
              foreground=[("readonly", fg_color)]
              )

    # Ensure non-ttk widgets are updated
    def update_widget(widget):
        """Recursively update the widget styles while skipping ttk widgets."""
        try:
            # Skip ttk widgets (they use styles instead of direct configuration)
            if isinstance(widget, ttk.Widget):
                return

            if isinstance(widget, (tk.Label, tk.Button, tk.Frame)):
                widget.configure(bg=bg_color, fg=fg_color)
            elif isinstance(widget, tk.Entry):
                widget.configure(bg=entry_bg, fg=fg_color, insertbackground=fg_color)

            # Recursively update child widgets
            for child in widget.winfo_children():
                update_widget(child)

        except AttributeError:
            pass  # Some widgets may not support these properties

    update_widget(root)

def apply_light_theme(root):
    """Applies a light theme."""
    apply_theme(root, "light")

def apply_dark_theme(root):
    """Applies a dark theme."""
    apply_theme(root, "dark")
