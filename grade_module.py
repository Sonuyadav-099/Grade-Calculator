# grade_module.py
# Simple grading logic (beginner style)

def get_grade(mark, average, highest):
    if mark == highest:
        return "S"
    elif mark > average:
        return "A"
    elif mark >= (average * 0.85):
        return "B"
    elif mark >= (average * 0.70):
        return "C"
    elif mark >= (average * 0.50):
        return "D"
    else:
        return "F"
