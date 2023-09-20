moves_count = int(input())
points = 0
numbers_between_zero_ten = 0
numbers_between_ten_twenty = 0
numbers_between_twenty_thirty = 0
numbers_between_thirty_forty = 0
number_between_forty_fifty = 0
invalid_numbers = 0

for i in range(moves_count):
    number = int(input())
    if 0 <= number < 10:
        points += number * 0.20
        numbers_between_zero_ten += 1
    elif 10 <= number < 20:
        points += number * 0.30
        numbers_between_ten_twenty += 1
    elif 20 <= number < 30:
        points += number * 0.40
        numbers_between_twenty_thirty += 1
    elif 30 <= number < 40:
        points += 50
        numbers_between_thirty_forty += 1
    elif 40 <= number <= 50:
        points += 100
        number_between_forty_fifty += 1
    elif number < 0 or number > 50:
        points /= 2
        invalid_numbers += 1

percent_numbers_between_zero_ten = numbers_between_zero_ten / moves_count * 100
percent_numbers_between_ten_twenty = numbers_between_ten_twenty / moves_count * 100
percent_numbers_between_twenty_thirty = numbers_between_twenty_thirty / moves_count * 100
percent_numbers_between_thirty_forty = numbers_between_thirty_forty / moves_count * 100
percent_number_between_forty_fifty = number_between_forty_fifty / moves_count * 100
percent_invalid_numbers = invalid_numbers / moves_count * 100

print(f"{points:.2f}")
print(f"From 0 to 9: {percent_numbers_between_zero_ten:.2f}%")
print(f"From 10 to 19: {percent_numbers_between_ten_twenty:.2f}%")
print(f"From 20 to 29: {percent_numbers_between_twenty_thirty:.2f}%")
print(f"From 30 to 39: {percent_numbers_between_thirty_forty:.2f}%")
print(f"From 40 to 50: {percent_number_between_forty_fifty:.2f}%")
print(f"Invalid numbers: {percent_invalid_numbers:.2f}%")
