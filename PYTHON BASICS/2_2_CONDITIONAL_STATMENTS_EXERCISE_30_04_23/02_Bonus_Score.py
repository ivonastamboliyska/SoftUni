current_points = int(input())
bonus_points = 0

if current_points <= 100:
    bonus_points = 5
elif current_points < 1000:
    bonus_points = 0.2 * current_points
elif current_points > 1000:
    bonus_points = 0.1 * current_points

additional_bonus_points = 0
if current_points % 2 == 0:
    additional_bonus_points = additional_bonus_points + 1
elif current_points % 10 == 5:
    additional_bonus_points = additional_bonus_points + 2

total_bonus_points = bonus_points + additional_bonus_points
print(total_bonus_points)
print(current_points + bonus_points + additional_bonus_points)


