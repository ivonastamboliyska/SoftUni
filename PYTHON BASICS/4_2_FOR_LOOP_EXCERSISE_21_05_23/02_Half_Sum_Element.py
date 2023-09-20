import sys
count_of_numbers = int(input())
max_number = - sys.maxsize
sum_of_numbers = 0

for numbers in range(count_of_numbers):
    current_number = int(input())
    if current_number > max_number:
        max_number = current_number
    sum_of_numbers += current_number

rest_sum = sum_of_numbers - max_number

if max_number == rest_sum:
    print(f"Yes\nSum = {max_number}")
else:
    diff = abs(max_number - rest_sum)
    print(f"No\nDiff = {diff}")