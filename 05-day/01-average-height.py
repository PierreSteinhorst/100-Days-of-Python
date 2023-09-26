# You are going to write a program that calculates the average student height from a List of heights.
student_heights = input("Input a list of student heights. ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0
total_students = 0

for student in student_heights:
    total_students += 1
for student in student_heights:
    total_height += student

avg_height = total_height / total_students
print(avg_height)

