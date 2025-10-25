import tkinter as tk
from ui import AudioPlayerUI

def main():
    root = tk.Tk()
    app = AudioPlayerUI(root)
    root.mainloop()
    
if __name__ == "__main__":
    main() 