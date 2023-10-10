student_scores = {
    "Marry": 83,
    "Ron": 78,
    "Hermine": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}


for entry in student_scores:
    if student_scores[entry] >= 91:
        print(f"{entry}: Outstanding")
    elif 81 <= student_scores[entry] < 91:
        print(f"{entry}: Exceeds Expectations")
    elif 71 <= student_scores[entry] < 80:
        print(f"{entry}: Acceptable")
    else:
        print(f"{entry}: Fail")