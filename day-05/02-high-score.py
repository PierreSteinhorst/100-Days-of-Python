# You are going to write a program that calculates the highest score from a List of scores.
students_scores = input("Input a list of students scores. ").split()
for n in range(0, len(students_scores)):
    students_scores[n] = int(students_scores[n])
print(students_scores)

max_score = 0
for score in students_scores:
    if score > max_score:
        max_score = score

print(f"The highest score in the class is: {max_score}")



