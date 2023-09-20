from math import ceil

name_of_series = input()
episode_length = int(input())
lunch_break_length = int(input())

time_for_eating = lunch_break_length / 8
time_for_relax = lunch_break_length / 4
time_left_for_watching = lunch_break_length - time_for_eating - time_for_relax

total_time_left = time_left_for_watching - episode_length
total_time_needed = episode_length - time_left_for_watching

if time_left_for_watching >= episode_length:
    print(f"You have enough time to watch {name_of_series} and left with {ceil(total_time_left)} minutes free time.")
elif time_left_for_watching < episode_length:
    print(f"You don't have enough time to watch {name_of_series}, you need {ceil(total_time_needed)} more minutes.")

