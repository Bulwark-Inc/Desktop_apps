import tkinter as tk
from gui import StopwatchTimer

def main():    
    root = tk.Tk()
    app = StopwatchTimer(root)
    root.mainloop()

if __name__ == "__main__":
    main()