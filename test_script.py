import student_code
import sys


def grade_activity_1():
    correct_overworked = ["Compressor", "Sensor", "Conveyor"]
    return sorted(student_code.overworked_equipment) == sorted(correct_overworked)


def grade_activity_2():
    correct_below_average = ["Pump", "Valve"]
    return sorted(student_code.below_average_operation) == sorted(correct_below_average)


def grade_assignment():
    score = 0
    if grade_activity_1():
        score += 1
    else:
        print("Activity 1 failed.")

    if grade_activity_2():
        score += 1
    else:
        print("Activity 2 failed.")

    if score == 2:
        sys.exit(0)  # Pass
    else:
        sys.exit(1)  # Fail


grade_assignment()
