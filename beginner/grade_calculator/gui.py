import tkinter as tk
from tkinter import messagebox

class GradeCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Grade Calculator")
        self.subjects = []  # Store subject data as (name, score, weight)

        # Labels and Entry Fields
        tk.Label(root, text="Subject:").grid(row=0, column=0)
        self.subject_entry = tk.Entry(root)
        self.subject_entry.grid(row=0, column=1)
        
        tk.Label(root, text="Score:").grid(row=1, column=0)
        self.score_entry = tk.Entry(root)
        self.score_entry.grid(row=1, column=1)
        
        tk.Label(root, text="Weight:").grid(row=2, column=0)
        self.weight_entry = tk.Entry(root)
        self.weight_entry.grid(row=2, column=1)
        
        # Buttons
        tk.Button(root, text="Add Subject", command=self.add_subject).grid(row=3, column=0, columnspan=2)
        tk.Button(root, text="Calculate GPA", command=self.calculate_gpa).grid(row=4, column=0, columnspan=2)
        
        # Results Display
        self.result_label = tk.Label(root, text="", justify="left")
        self.result_label.grid(row=5, column=0, columnspan=2)

    def add_subject(self):
        name = self.subject_entry.get()
        score = self.score_entry.get()
        weight = self.weight_entry.get()
        
        if not name or not score or not weight:
            messagebox.showerror("Input Error", "All fields are required!")
            return
        
        try:
            score = float(score)
            weight = float(weight)
        except ValueError:
            messagebox.showerror("Input Error", "Score and Weight must be numbers!")
            return
        
        self.subjects.append((name, score, weight))
        self.subject_entry.delete(0, tk.END)
        self.score_entry.delete(0, tk.END)
        self.weight_entry.delete(0, tk.END)
        self.update_results()

    def calculate_gpa(self):
        if not self.subjects:
            messagebox.showerror("Calculation Error", "No subjects added!")
            return
        
        total_weighted_scores = sum(score * weight for _, score, weight in self.subjects)
        total_weights = sum(weight for _, _, weight in self.subjects)
        gpa = total_weighted_scores / total_weights if total_weights else 0
        
        self.result_label.config(text=f"Your GPA: {gpa:.2f}")
    
    def update_results(self):
        display_text = "Subjects Added:\n"
        for name, score, weight in self.subjects:
            display_text += f"{name}: Score = {score}, Weight = {weight}\n"
        self.result_label.config(text=display_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = GradeCalculator(root)
    root.mainloop()
