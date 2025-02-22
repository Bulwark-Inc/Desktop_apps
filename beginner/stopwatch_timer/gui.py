import tkinter as tk
from tkinter import messagebox
from logic import StopwatchTimerLogic  # Import the logic class

class StopwatchTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch & Timer")
        self.root.geometry("400x500")
        self.root.configure(bg="#1E2A38")

        self.watch = StopwatchTimerLogic()  # Instantiate logic class
        self.time_var = tk.StringVar()
        self.time_var.set("00:00")

        # Mode Selection
        self.mode_var = tk.StringVar(value="stopwatch")
        self.mode_frame = tk.Frame(root)
        self.mode_frame.pack(pady=5)

        self.stopwatch_btn = tk.Radiobutton(self.mode_frame, text="Stopwatch", variable=self.mode_var, value="stopwatch", command=self.switch_mode)
        self.timer_btn = tk.Radiobutton(self.mode_frame, text="Timer", variable=self.mode_var, value="timer", command=self.switch_mode)

        self.stopwatch_btn.pack(side="left", padx=10)
        self.timer_btn.pack(side="right", padx=10)

        # Time Display
        self.time_display = tk.Label(root, textvariable=self.time_var, font=("Arial", 30), fg="white", bg="#1E2A38")
        self.time_display.pack(pady=20)

        # Timer Input (Initially Hidden)
        self.timer_input = tk.Entry(root, font=("Arial", 12), width=10)
        
        # Buttons
        self.start_button = tk.Button(root, text="Start", font=("Arial", 12), bg="#28A745", fg="white", command=self.start)
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(root, text="Stop", font=("Arial", 12), bg="#DC3545", fg="white", command=self.stop)
        self.stop_button.pack(pady=5)

        self.reset_button = tk.Button(root, text="Reset", font=("Arial", 12), bg="#FFC107", fg="black", command=self.reset)
        self.reset_button.pack(pady=5)

        self.lap_button = tk.Button(root, text="Lap", font=("Arial", 12), bg="#17A2B8", fg="white", command=self.record_lap)
        self.lap_button.pack(pady=5)

        # Lap Display
        self.lap_listbox = tk.Listbox(root, font=("Arial", 12), height=6)
        self.lap_listbox.pack(pady=10, fill=tk.BOTH, expand=True)

    def update_display(self):
        """Updates the displayed time based on the current mode."""
        if self.watch.running:
            self.time_var.set(self.watch.get_time())
            self.root.after(100, self.update_display)  # Refresh every 100ms

    def switch_mode(self):
        """Switches between Stopwatch and Timer mode."""
        self.watch.mode = self.mode_var.get()
        self.watch.reset()

        # Show timer input field if in timer mode
        self.timer_input.pack_forget()
        if self.watch.mode == "timer":
            self.timer_input.pack()

    def start(self):
        """Starts the stopwatch or timer."""
        if self.watch.mode == "timer":
            try:
                seconds = int(self.timer_input.get())
                if seconds <= 0:
                    raise ValueError
                self.watch.set_timer(seconds)
            except ValueError:
                messagebox.showerror("Invalid Input", "Enter a valid number of seconds.")
                return

        self.watch.start()
        self.update_display()

    def stop(self):
        self.watch.pause()

    def reset(self):
        self.watch.reset()
        self.time_var.set("00:00")
        self.lap_listbox.delete(0, tk.END)

    def record_lap(self):
        if self.watch.running:
            lap_time = self.watch.get_time()
            self.lap_listbox.insert(tk.END, f"Lap {self.lap_listbox.size() + 1}: {lap_time}")
