from datetime import datetime
import pytz
from utils import validate_time_format, get_all_timezones, format_converted_time

class TimeZoneConverter:
    """
    Handles time conversion between different time zones.
    """

    def __init__(self):
        self.available_timezones = get_all_timezones()

    def convert_time(self, time_str: str, source_tz: str, target_tz: str) -> str:
        """
        Converts a given time from one time zone to another.

        :param time_str: Time input as a string (e.g., "12:30 PM", "23:45").
        :param source_tz: Source time zone (e.g., "America/New_York").
        :param target_tz: Target time zone (e.g., "Asia/Tokyo").
        :return: Formatted string of the converted time or an error message.
        """
        if source_tz not in self.available_timezones:
            return f"Error: Invalid source time zone '{source_tz}'"
        if target_tz not in self.available_timezones:
            return f"Error: Invalid target time zone '{target_tz}'"

        # Validate and parse time input
        parsed_time = validate_time_format(time_str)
        if not parsed_time:
            return "Error: Invalid time format. Use 'HH:MM AM/PM' or 'HH:MM' (24-hour format)."

        # Attach source time zone
        source_timezone = pytz.timezone(source_tz)
        localized_time = source_timezone.localize(parsed_time)

        # Convert to target time zone
        target_timezone = pytz.timezone(target_tz)
        converted_time = localized_time.astimezone(target_timezone)

        # Format and return the result
        return format_converted_time(converted_time, target_tz)
