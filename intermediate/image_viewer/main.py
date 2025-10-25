from viewer import ImageViewer
import tkinter as tk

def main():
    root = tk.Tk()  # Create the main window
    app = ImageViewer(root)  # Initialize the ImageViewer class
    root.mainloop()  # Run the Tkinter event loop

if __name__ == "__main__":
    main()
