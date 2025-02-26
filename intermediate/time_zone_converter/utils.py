from datetime import datetime
import tkinter as tk
from tkinter import ttk
import pytz

class AutoCompleteCombobox(ttk.Combobox):
    """
    A custom Combobox with an autocomplete feature.
    """
    def set_completion_list(self, completion_list):
        """Set a new autocomplete list."""
        self._completion_list = sorted(completion_list)
        self._hits = []
        self._hit_index = 0
        self.position = 0
        self.bind('<KeyRelease>', self._on_keyrelease)

    def _on_keyrelease(self, event):
        """Filter the dropdown list based on user input."""
        if event.keysym in ["BackSpace", "Left", "Right", "Up", "Down"]:
            return

        value = self.get()
        if value == '':
            self['values'] = self._completion_list
        else:
            matches = [item for item in self._completion_list if item.lower().startswith(value.lower())]
            self['values'] = matches

        self.event_generate('<Down>')  # Open dropdown

def validate_time_format(time_str: str) -> datetime:
    """
    Validates and parses a time string in 12-hour or 24-hour format.

    :param time_str: Time string input (e.g., "12:30 PM" or "23:45").
    :return: Parsed datetime object if valid, else None.
    """
    time_formats = ["%I:%M %p", "%H:%M"]  # 12-hour and 24-hour formats

    for fmt in time_formats:
        try:
            return datetime.strptime(time_str, fmt)
        except ValueError:
            continue  # Try the next format

    return None  # Invalid format

def get_all_timezones() -> list:
    """
    Returns a sorted list of all available time zones.

    :return: List of time zone names.
    """
    return sorted(pytz.all_timezones)

def format_converted_time(time_obj: datetime, tz_name: str) -> str:
    """
    Formats a datetime object into a readable time with time zone info.

    :param time_obj: Converted datetime object.
    :param tz_name: Time zone name.
    :return: Formatted time string.
    """
    tz = pytz.timezone(tz_name)
    localized_time = time_obj.astimezone(tz)
    return localized_time.strftime("%I:%M %p (%Z)")  # Example: "10:30 AM (PST)"
