location_count = int(input())
gold_collected = 0
days_collecting_gold = 0
expected_average_gold_per_day = 0

for location in range(location_count):
    expected_average_gold_per_day = float(input())
    days_collecting_gold = int(input())
    for days in range(days_collecting_gold):
        average_gold_per_day = float(input())
        gold_collected += average_gold_per_day
    average_gold_collected = gold_collected / days_collecting_gold
    if average_gold_collected >= expected_average_gold_per_day:
        print(f"Good job! Average gold per day: {average_gold_collected:.2f}.")
    else:
        difference = expected_average_gold_per_day - average_gold_collected
        print(f"You need {difference:.2f} gold.")
    gold_collected = 0

