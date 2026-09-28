# stats_module.py
# Calculates averages and highest marks

def calculate_average(marks_list):
    return sum(marks_list) / len(marks_list)

def find_highest(marks_list):
    highest = marks_list[0]
    for m in marks_list[1:]:
        if m > highest:
            highest = m
    return highest
