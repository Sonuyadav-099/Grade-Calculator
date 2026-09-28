# input_module.py
# Handles student input and validation

def get_valid_marks(subject, max_marks):
    marks = float(input(f"Marks in {subject}: "))
    while marks < 0 or marks > max_marks:
        print("Invalid! Marks must be between 0 and", max_marks)
        marks = float(input(f"Marks in {subject}: "))
    return marks
