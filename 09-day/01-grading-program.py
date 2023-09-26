student_scores = {
    "Marry": 83,
    "Ron": 78,
    "Hermine": 99,
    "Draco": 74,
    "Neville": 62,
}

# Write a program that converts their scores to grades.
# score 91 - 100: "Outstanding"
# score 81 - 90: "Exceeds Expectations"
# score 71 - 80: "Acceptable"
student_grades = {}
for student in student_scores:
    if 91 <= student_scores[student] <= 100:
        student_grades[student] = "Outstanding"
    elif 81 <= student_scores[student] <= 90:
        student_grades[student] = "Exceeds Expectations"
    elif 71 <= student_scores[student] <= 80:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)
