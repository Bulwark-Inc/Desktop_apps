from gui import PasswordApp
import tkinter as tk

def main():
    root = tk.Tk()
    app = PasswordApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()