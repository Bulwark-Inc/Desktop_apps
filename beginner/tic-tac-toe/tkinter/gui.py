import tkinter as tk
from tkinter import messagebox
import pygame  # For sounds
from logic import TicTacToe

class TicTacToeGUI:
    def __init__(self, root):
        """Initialize the Tic-Tac-Toe game GUI with sounds."""
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.configure(bg="#1E1E1E")  # Dark mode background

        # Initialize pygame mixer for sound
        pygame.mixer.init()
        self.click_sound = pygame.mixer.Sound("sounds/click.wav")
        self.win_sound = pygame.mixer.Sound("sounds/win.wav")
        self.draw_sound = pygame.mixer.Sound("sounds/draw.wav")

        self.game = TicTacToe()
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        # Title Label
        self.title_label = tk.Label(root, text="Tic-Tac-Toe", font=("Arial", 24, "bold"),
                                    fg="#00FF00", bg="#1E1E1E")
        self.title_label.grid(row=0, column=0, columnspan=3, pady=10)

        # **Player Turn Indicator**
        self.turn_label = tk.Label(root, text="Player X's Turn", font=("Arial", 16, "bold"),
                                   fg="white", bg="#1E1E1E")
        self.turn_label.grid(row=1, column=0, columnspan=3, pady=5)

        # **Scoreboard**
        self.score_x = 0
        self.score_o = 0
        self.score_draw = 0
        self.score_label = tk.Label(root, text=f"X: {self.score_x}  |  O: {self.score_o}  |  Draws: {self.score_draw}",
                                    font=("Arial", 14, "bold"), fg="cyan", bg="#1E1E1E")
        self.score_label.grid(row=2, column=0, columnspan=3, pady=5)

        # **Game Buttons (3x3 Grid)**
        for row in range(3):
            for col in range(3):
                btn = tk.Button(root, text="", font=("Arial", 24, "bold"),
                                width=5, height=2, bg="#1F6FEB", fg="white",
                                activebackground="#00FF00",
                                command=lambda r=row, c=col: self.on_click(r, c))
                btn.grid(row=row+3, column=col, padx=1, pady=1)
                btn.bind("<Enter>", self.on_hover)
                btn.bind("<Leave>", self.on_leave)
                self.buttons[row][col] = btn

        # **Restart Button**
        self.reset_button = tk.Button(root, text="Restart", font=("Arial", 16, "bold"),
                                      fg="white", bg="#FF0000", activebackground="#FF6666",
                                      command=self.reset_game)
        self.reset_button.grid(row=6, column=0, columnspan=3, pady=10)

    def on_click(self, row, col):
        """Handles button click events."""
        if self.game.make_move(row, col):
            self.click_sound.play()  # **Play Click Sound**
            self.buttons[row][col].config(text=self.game.current_player)

            # Check for winner
            result = self.game.check_winner()
            if result:
                if result == "X":
                    self.score_x += 1
                elif result == "O":
                    self.score_o += 1
                else:
                    self.score_draw += 1
                
                # **Play Win or Draw Sound**
                if result == "Draw":
                    self.draw_sound.play()
                else:
                    self.win_sound.play()

                messagebox.showinfo("Game Over", f"{result} Wins!" if result != "Draw" else "It's a Draw!")
                self.update_scoreboard()
                self.reset_game()
                return
            
            self.game.switch_player()
            self.update_turn_label()

    def update_turn_label(self):
        """Updates the turn indicator label."""
        self.turn_label.config(text=f"Player {self.game.current_player}'s Turn", fg="#00FF00" if self.game.current_player == "X" else "#FFA500")

    def update_scoreboard(self):
        """Updates the scoreboard after each game."""
        self.score_label.config(text=f"X: {self.score_x}  |  O: {self.score_o}  |  Draws: {self.score_draw}")

    def reset_game(self):
        """Resets the game board."""
        self.game.reset_game()
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="")
        self.update_turn_label()

    def on_hover(self, event):
        """Button hover effect."""
        event.widget.config(bg="#FFDD44")

    def on_leave(self, event):
        """Removes hover effect."""
        event.widget.config(bg="#1F6FEB")
