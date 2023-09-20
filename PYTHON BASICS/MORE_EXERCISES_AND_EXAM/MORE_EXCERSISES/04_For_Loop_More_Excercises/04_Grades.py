students_count = int(input())
failed_students_count = 0
students_under_four = 0
students_under_five = 0
excellent_students = 0
total_grades = 0

for i in range(students_count):
    grade = float(input())
    if grade < 3:
        failed_students_count += 1
        total_grades += grade
    elif grade < 4:
        students_under_four += 1
        total_grades += grade
    elif grade < 5:
        students_under_five += 1
        total_grades += grade
    elif grade >= 5:
        excellent_students += 1
        total_grades += grade

average_grade = total_grades / students_count
percent_failed_students = failed_students_count / students_count * 100
percent_students_under_four = students_under_four / students_count * 100
percent_students_under_five = students_under_five / students_count * 100
percent_excellent_students = excellent_students / students_count * 100

print(f"Top students: {percent_excellent_students:.2f}%")
print(f"Between 4.00 and 4.99: {percent_students_under_five:.2f}%")
print(f"Between 3.00 and 3.99: {percent_students_under_four:.2f}%")
print(f"Fail: {percent_failed_students:.2f}%")
print(f"Average: {average_grade:.2f}")
