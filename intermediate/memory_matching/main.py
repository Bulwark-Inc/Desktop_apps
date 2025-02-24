import tkinter as tk
from logic import MemoryGame

def main():
    """Main function to start the Memory Matching Game."""
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
