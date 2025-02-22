import time

class StopwatchTimerLogic:
    def __init__(self):
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0
        self.timer_duration = 0  # Countdown duration
        self.mode = "stopwatch"

    def start(self):
        """Starts the stopwatch or timer."""
        if not self.running:
            self.running = True
            self.start_time = time.time() - self.elapsed_time

    def pause(self):
        """Pauses the stopwatch or timer."""
        if self.running:
            self.running = False
            self.elapsed_time = time.time() - self.start_time

    def reset(self):
        """Resets the stopwatch or timer."""
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0
        self.timer_duration = 0

    def set_timer(self, seconds):
        """Sets the timer duration for countdown mode."""
        self.timer_duration = seconds
        self.elapsed_time = 0  # Reset elapsed time for new countdown

    def get_time(self):
        """Returns formatted time."""
        if self.running:
            elapsed = time.time() - self.start_time
        else:
            elapsed = self.elapsed_time

        if self.mode == "stopwatch":
            return self.format_time(elapsed)
        else:
            remaining = max(0, self.timer_duration - elapsed)
            return self.format_time(remaining) if remaining > 0 else "00:00"

    @staticmethod
    def format_time(seconds):
        """Formats time as MM:SS:MS."""
        minutes = int(seconds // 60)
        seconds = int(seconds % 60)
        milliseconds = int((seconds * 100) % 100)
        return f"{minutes:02}:{seconds:02}:{milliseconds:02}"
