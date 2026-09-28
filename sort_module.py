# sort_module.py
# Bubble sort written in a very basic way (like a student would do)

def bubble_sort(names, totals, subjects):
    n = len(totals)
    print("\nSorting students by total marks using Bubble Sort...")

    # Outer loop
    for i in range(n):
        # Inner loop
        for j in range(0, n - i - 1):
            if totals[j] < totals[j + 1]:
                # Swap totals
                temp = totals[j]
                totals[j] = totals[j + 1]
                totals[j + 1] = temp

                # Swap names
                temp_name = names[j]
                names[j] = names[j + 1]
                names[j + 1] = temp_name

                # Swap marks for each subject
                for s in subjects:
                    temp_marks = s[j]
                    s[j] = s[j + 1]
                    s[j + 1] = temp_marks

    print("Sorting done.\n")

