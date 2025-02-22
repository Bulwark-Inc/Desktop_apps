import tkinter as tk
from tkinter import messagebox
import random

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcard App")
        self.root.geometry("400x300")

        self.flashcards = []
        self.current_index = 0
        self.showing_answer = False

        self.card_label = tk.Label(root, text="Add Flashcards", font=("Arial", 16), wraplength=350, pady=20)
        self.card_label.pack()

        self.flip_button = tk.Button(root, text="Flip", command=self.flip_card)
        self.flip_button.pack()

        self.next_button = tk.Button(root, text="Next", command=self.next_card)
        self.next_button.pack()

        self.prev_button = tk.Button(root, text="Previous", command=self.prev_card)
        self.prev_button.pack()

        self.shuffle_button = tk.Button(root, text="Shuffle", command=self.shuffle_cards)
        self.shuffle_button.pack()

        self.add_frame = tk.Frame(root)
        self.add_frame.pack(pady=10)

        self.question_entry = tk.Entry(self.add_frame, width=30)
        self.question_entry.grid(row=0, column=0, padx=5)
        self.answer_entry = tk.Entry(self.add_frame, width=30)
        self.answer_entry.grid(row=1, column=0, padx=5)
        
        self.add_button = tk.Button(self.add_frame, text="Add", command=self.add_flashcard)
        self.add_button.grid(row=2, column=0, pady=5)

    def add_flashcard(self):
        question = self.question_entry.get()
        answer = self.answer_entry.get()
        if question and answer:
            self.flashcards.append((question, answer))
            self.question_entry.delete(0, tk.END)
            self.answer_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Flashcard added!")
            self.current_index = len(self.flashcards) - 1
            self.update_card_display()
        else:
            messagebox.showerror("Error", "Both fields are required!")

    def flip_card(self):
        if self.flashcards:
            self.showing_answer = not self.showing_answer
            self.update_card_display()
        else:
            messagebox.showerror("Error", "No flashcards available!")

    def next_card(self):
        if self.flashcards:
            self.current_index = (self.current_index + 1) % len(self.flashcards)
            self.showing_answer = False
            self.update_card_display()

    def prev_card(self):
        if self.flashcards:
            self.current_index = (self.current_index - 1) % len(self.flashcards)
            self.showing_answer = False
            self.update_card_display()

    def shuffle_cards(self):
        if self.flashcards:
            random.shuffle(self.flashcards)
            self.current_index = 0
            self.showing_answer = False
            self.update_card_display()

    def update_card_display(self):
        if self.flashcards:
            text = self.flashcards[self.current_index][1] if self.showing_answer else self.flashcards[self.current_index][0]
        else:
            text = "Add Flashcards"
        self.card_label.config(text=text)

