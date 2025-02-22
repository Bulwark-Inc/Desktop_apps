import random

class FlashcardApp:
    def __init__(self):
        self.flashcards = [
            {"question": "What is the capital of France?", "answer": "Paris"},
            {"question": "What is 2 + 2?", "answer": "4"},
            {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"}
        ]
        self.current_index = 0
        self.show_question = True  # True: show question, False: show answer
    
    def get_current_flashcard(self):
        """Returns the current flashcard text based on the state."""
        card = self.flashcards[self.current_index]
        return card["question"] if self.show_question else card["answer"]
    
    def flip_flashcard(self):
        """Flips the flashcard to show either the question or answer."""
        self.show_question = not self.show_question
    
    def next_flashcard(self):
        """Moves to the next flashcard."""
        if self.current_index < len(self.flashcards) - 1:
            self.current_index += 1
            self.show_question = True
    
    def previous_flashcard(self):
        """Moves to the previous flashcard."""
        if self.current_index > 0:
            self.current_index -= 1
            self.show_question = True
    
    def shuffle_flashcards(self):
        """Shuffles the flashcards randomly."""
        random.shuffle(self.flashcards)
        self.current_index = 0
        self.show_question = True
