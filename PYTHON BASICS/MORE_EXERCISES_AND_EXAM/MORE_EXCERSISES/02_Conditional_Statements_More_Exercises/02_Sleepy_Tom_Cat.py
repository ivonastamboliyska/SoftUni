free_days_count = int(input())

minutes_on_working_day = 63
minutes_free_days = 127
total_days_in_a_year = 365
norm_for_games = 30000

working_days = total_days_in_a_year - free_days_count
total_minutes_on_working_days = working_days * minutes_on_working_day
total_minutes_on_free_days = free_days_count * minutes_free_days
total_minutes_for_games = total_minutes_on_free_days + total_minutes_on_working_days

if total_minutes_for_games > norm_for_games:
    print("Tom will run away")
    difference = total_minutes_for_games - norm_for_games
    difference_in_hours = difference // 60
    difference_in_minutes = difference % 60
    print(f"{difference_in_hours} hours and {difference_in_minutes} minutes more for play")

elif total_minutes_for_games < norm_for_games:
    print("Tom sleeps well")
    differ = norm_for_games - total_minutes_for_games
    differ_in_hours = differ // 60
    differ_in_minutes = differ % 60
    print(f"{differ_in_hours} hours and {differ_in_minutes} minutes less for play")

# На конзолата трябва да се отпечатат два реда.
# •	Ако времето за игра на Том е над нормата за текущата година:
# o	 На първия ред отпечатайте: “Tom will run away”
# o	 На втория ред отпечатайте разликата от нормата във формат:
# “{H} hours and {M} minutes more for play”
# •	Ако времето за игра на Том е под нормата за текущата година:
# o	На първия ред отпечатайте: “Tom sleeps well”
# o	 На втория ред отпечатайте разликата от нормата във формат:
# “{H} hours and {M} minutes less for play”
