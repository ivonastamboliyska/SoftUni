count_of_numbers = int(input())
odd_position = 0
even_position = 0
sum_of_numbers = 0

for numbers in range(count_of_numbers):
    current_number = int(input())
    if numbers % 2 == 0:
        even_position += current_number
    else:
        odd_position += current_number


if even_position == odd_position:
    print(f"Yes\n Sum = {odd_position}")
else:
    difference = abs(even_position - odd_position)
    print(f"No\n Diff = {difference}")

