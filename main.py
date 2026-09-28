# main.py
# Entry point of the Grade Calculator Project
# Written in a simple beginner style

from input_module import get_valid_marks
from grade_module import get_grade
from stats_module import calculate_average, find_highest
from sort_module import bubble_sort
from report_module import print_report

print("===================================")
print("   Welcome to the Grade Calculator ")
print("===================================\n")

# Ask for number of students
num_students = int(input("How many students? (Enter at least 2): "))
while num_students < 2:
    print("Error: You must enter 2 or more students.")
    num_students = int(input("How many students? (Enter at least 2): "))

# Ask for maximum marks
max_marks = float(input("Enter maximum marks for a subject: "))
print("Okay, maximum marks set to", max_marks, "\n")

# Lists to store data
names = []
calc_marks = []
prog_marks = []
evs_marks = []
eng_marks = []
totals = []

# Collect student data
for i in range(num_students):
    print("\n--- Entering data for Student", i + 1, "---")
    name = input("Enter student name: ")
    names.append(name)

    m1 = get_valid_marks("Calculus", max_marks)
    m2 = get_valid_marks("Programming Language", max_marks)
    m3 = get_valid_marks("EVS", max_marks)
    m4 = get_valid_marks("English", max_marks)

    calc_marks.append(m1)
    prog_marks.append(m2)
    evs_marks.append(m3)
    eng_marks.append(m4)

    total = m1 + m2 + m3 + m4
    totals.append(total)

    print("Data saved for", name)

print("\nAll student data collected successfully!\n")

# Calculate averages
calc_avg = calculate_average(calc_marks)
prog_avg = calculate_average(prog_marks)
evs_avg = calculate_average(evs_marks)
eng_avg = calculate_average(eng_marks)
averages = {
    "Calculus": calc_avg,
    "Programming": prog_avg,
    "EVS": evs_avg,
    "English": eng_avg
}

# Find highest marks
calc_high = find_highest(calc_marks)
prog_high = find_highest(prog_marks)
evs_high = find_highest(evs_marks)
eng_high = find_highest(eng_marks)
highs = {
    "Calculus": calc_high,
    "Programming": prog_high,
    "EVS": evs_high,
    "English": eng_high
}

print("Now sorting students by total marks...\n")

# Sort students
bubble_sort(names, totals, [calc_marks, prog_marks, evs_marks, eng_marks])

# Show final report
print_report(
    names,
    {"Calculus": calc_marks, "Programming": prog_marks, "EVS": evs_marks, "English": eng_marks},
    totals,
    averages,
    highs,
    get_grade
)

print("Program finished. Thank you for using Grade Calculator!\n")
