import random
import os
import tkinter as tk
from card import Card

class MemoryGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Memory Matching Game")
        self.card_back_image = "images/card_back.png"
        self.grid_size = (4, 5)  # Rows, Columns

        # Load card front images dynamically
        image_folder = "images"
        self.card_images = [os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.endswith(".png") and "card_back" not in img]

        # Duplicate, shuffle, and create Card objects
        self.cards = self.card_images * 2  # Each image appears twice
        random.shuffle(self.cards)
        
        self.card_objects = []
        self.selected_cards = []
        self.matched_pairs = 0
        self.locked = False
        self.total_pairs = len(self.cards) // 2
        self.moves = 0
        self.game_started = False
        self.time_elapsed = 0

        # UI elements
        self.timer_label = tk.Label(self.master, text="⏳ Time: 0 sec", font=("Arial", 14))
        self.timer_label.grid(row=0, column=0, columnspan=2)

        self.moves_label = tk.Label(self.master, text="📋 Moves: 0", font=("Arial", 14))
        self.moves_label.grid(row=0, column=2, columnspan=2)

        self.create_board()

    def start_timer(self):
        """Starts the game timer only once."""
        if not self.game_started:
            self.game_started = True
            self.time_elapsed = 0
            self.update_timer()

    def update_timer(self):
        """Updates the timer every second."""
        self.time_elapsed += 1
        self.timer_label.config(text=f"⏳ Time: {self.time_elapsed} sec")
        self.timer_id = self.master.after(1000, self.update_timer)  # Save the ID to cancel later


    def create_board(self):
        """Creates a grid layout for the memory game."""
        rows, cols = self.grid_size
        for row in range(rows):
            for col in range(cols):
                index = row * cols + col
                if index < len(self.cards):
                    card = Card(self.master, self.cards[index], self.card_back_image, row, col, self.on_card_click)
                    card.button.grid(row=row+1, column=col, padx=10, pady=10)  # Add padding
                    self.card_objects.append(card)

    def on_card_click(self, card):
        """Handles card clicks, preventing more than two selections at once."""
        if not self.game_started:
            self.start_timer()  # Start timer when first card is clicked

        if self.locked or len(self.selected_cards) >= 2 or card in self.selected_cards:
            return  # Ignore if already selected

        card.reveal()
        self.selected_cards.append(card)

        if len(self.selected_cards) == 2:
            self.moves += 1  # Increase move count only when two cards are picked
            self.moves_label.config(text=f"📋 Moves: {self.moves}")
            self.locked = True
            self.master.after(1000, self.check_match)  # Delay match check

    def check_match(self):
        """Checks if two selected cards match and unlocks the game after checking."""
        if len(self.selected_cards) < 2:
            return  

        card1, card2 = self.selected_cards  

        if card1.front_image_path == card2.front_image_path:
            card1.disable()
            card2.disable()
            self.matched_pairs += 1  # Track matched pairs
        else:
            self.master.after(500, lambda: (card1.hide(), card2.hide()))  # Hide unmatched cards after delay

        self.selected_cards.clear()
        self.locked = False  # Unlock for the next move

        if self.matched_pairs == self.total_pairs:
            self.show_win_message()

    def show_win_message(self):
        """Displays a message when the game is won and stops the timer."""
        self.master.after_cancel(self.timer_id)  # Stop the timer
        win_label = tk.Label(self.master, text=f"🎉 You Win in {self.time_elapsed} sec! 🎉", 
                            font=("Arial", 20), fg="green")
        win_label.grid(row=len(self.grid_size)+1, column=0, columnspan=self.grid_size[1])

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()
