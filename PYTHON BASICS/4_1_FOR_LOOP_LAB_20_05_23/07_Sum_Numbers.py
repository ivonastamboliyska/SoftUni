import sys
count_of_numbers = int(input())
min_number = sys.maxsize
max_num = - sys.maxsize
sum_of_number = 0
for num in range(count_of_numbers):
    current_number = int(input())
    sum_of_number += current_number

print(sum_of_number)
