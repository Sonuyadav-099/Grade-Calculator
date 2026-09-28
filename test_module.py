# test_module.py
# Very simple testing file (beginner style)

from grade_module import get_grade

def run_tests():
    print("Starting tests for get_grade function...\n")

    # Test 1: Highest marks should give 'S'
    result1 = get_grade(90, 80, 90)
    if result1 == "S":
        print("Test 1 Passed: Highest marks gave 'S'")
    else:
        print("Test 1 Failed: Expected 'S', got", result1)

    # Test 2: Above average should give 'A'
    result2 = get_grade(85, 80, 90)
    if result2 == "A":
        print("Test 2 Passed: Above average gave 'A'")
    else:
        print("Test 2 Failed: Expected 'A', got", result2)

    # Test 3: Around 70% of average should give 'C'
    result3 = get_grade(70, 80, 90)
    if result3 == "C":
        print("Test 3 Passed: 70% gave 'C'")
    else:
        print("Test 3 Failed: Expected 'C', got", result3)

    # Test 4: Very low marks should give 'F'
    result4 = get_grade(20, 80, 90)
    if result4 == "F":
        print("Test 4 Passed: Low marks gave 'F'")
    else:
        print("Test 4 Failed: Expected 'F', got", result4)

    print("\nTesting finished.")

if __name__ == "__main__":
    run_tests()
