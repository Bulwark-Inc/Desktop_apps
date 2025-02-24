import tkinter as tk
from PIL import Image, ImageTk  # Use PIL for better image handling

class Card:
    def __init__(self, master, front_image_path, back_image_path, row, col, on_click):
        """Represents a single card in the memory matching game."""
        self.master = master
        self.front_image_path = front_image_path
        self.back_image_path = back_image_path
        self.revealed = False
        self.row = row
        self.col = col
        self.on_click = on_click
        
        # Load images with resizing
        self.front_image = ImageTk.PhotoImage(Image.open(front_image_path).resize((100, 100)))
        self.back_image = ImageTk.PhotoImage(Image.open(back_image_path).resize((100, 100)))

        # Create button for the card
        self.button = tk.Button(master, image=self.back_image, command=self.handle_click)
        self.button.grid(row=row, column=col, padx=5, pady=5)

    def handle_click(self):
        """Passes control to the game logic instead of flipping immediately."""
        self.on_click(self)

    def reveal(self):
        """Reveals the card image when clicked."""
        if not self.revealed:
            self.button.config(image=self.front_image)
            self.revealed = True
    
    def hide(self):
        """Hides the card again if not matched."""
        self.button.config(image=self.back_image)
        self.revealed = False
    
    def disable(self):
        """Disables the button when matched."""
        self.button.config(state=tk.DISABLED)
