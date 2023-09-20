import math

tournaments_count = int(input())
starting_points = int(input())
points_won = 0
tournaments_won = 0

for _ in range(tournaments_count):
    stage_reached = input()
    if stage_reached == "W":
        points_won += 2000
        tournaments_won += 1
    elif stage_reached == "F":
        points_won += 1200
    elif stage_reached == "SF":
        points_won += 720

total_points = starting_points + points_won
average_points = points_won / tournaments_count
math.floor(average_points)

tournaments_percent = tournaments_won / tournaments_count * 100

print(f"Final points: {total_points}")
print(f"Average points: {int(average_points)}")
print(f"{tournaments_percent:.2f}%")