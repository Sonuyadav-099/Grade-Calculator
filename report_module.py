# report_module.py
# Prints the report cards in a simple way

def print_report(names, subjects, totals, averages, highs, grade_func):
    print("\n==============================")
    print("Class Averages:")
    for subject, avg in averages.items():
        print(subject, ":", round(avg, 2))
    overall_avg = sum(totals) / len(totals)
    print("Overall Average:", round(overall_avg, 2))
    print("==============================\n")

    print("Report Cards (Ranked Highest to Lowest)")
    for i in range(len(names)):
        print("\nRank", i + 1, "-", names[i])
        # Print each subject marks and grade
        for subject in subjects.keys():
            mark = subjects[subject][i]
            grade = grade_func(mark, averages[subject], highs[subject])
            print(subject, ":", mark, "-> Grade:", grade)

        # Print total marks and overall grade
        total_marks = totals[i]
        overall_grade = grade_func(total_marks, overall_avg, max(totals))
        print("Total:", total_marks, "-> Overall Grade:", overall_grade)

    print("\nEnd of Report.\n")

