tasks_count = 0
bad_grades_count = 0
grades_sum = 0
last_task_name = ""
average_grade = 0

failed_threshold = int(input())

is_failed = False
while True:
    current_task = input()
    if current_task == "Enough":
        break

    current_grade = int(input())
    grades_sum += current_grade
    tasks_count += 1

    if current_grade <= 4:
        bad_grades_count += 1
        if bad_grades_count >= failed_threshold:
            is_failed = True
            break

    average_grade_grade = grades_sum / tasks_count

if not is_failed:
    print(f"Average score: {average_grade :.2f}")
    print(f"Number of problems: {tasks_count}")
    print(f"Last problem: {last_task_name}")
else:
    print(f"You need a break, {bad_grades_count} poor grades.")

