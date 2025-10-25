class GradeCalculator:
    def __init__(self):
        self.grades = []  # Stores (subject, score, weight)
    
    def add_grade(self, subject, score, weight=1):
        """Adds a grade with an optional weight."""
        try:
            score = float(score)
            weight = float(weight)
            if 0 <= score <= 100 and weight > 0:
                self.grades.append((subject, score, weight))
            else:
                return "Invalid score or weight"
        except ValueError:
            return "Invalid input"
    
    def calculate_weighted_average(self):
        """Calculates the weighted average of grades."""
        if not self.grades:
            return "No grades entered"
        
        total_weighted_score = sum(score * weight for _, score, weight in self.grades)
        total_weight = sum(weight for _, _, weight in self.grades)
        return round(total_weighted_score / total_weight, 2)
    
    def calculate_gpa(self):
        """Converts the weighted average to a GPA scale."""
        avg = self.calculate_weighted_average()
        if isinstance(avg, str):  # If there's an error
            return avg
        
        if avg >= 90:
            return 4.0
        elif avg >= 80:
            return 3.5
        elif avg >= 70:
            return 3.0
        elif avg >= 60:
            return 2.5
        elif avg >= 50:
            return 2.0
        else:
            return 0.0

    def reset_grades(self):
        """Clears all stored grades."""
        self.grades.clear()
        return "Grades cleared"
