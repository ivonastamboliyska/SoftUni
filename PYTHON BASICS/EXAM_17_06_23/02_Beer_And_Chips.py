from math import ceil
fan_name = input()
budget = float(input())
beer_count = int(input())
chips_count = int(input())

beer_price = 1.20

total_amount_for_beer = beer_count * beer_price
total_amount_for_chips = (total_amount_for_beer * 0.45) * chips_count

total_spend = ceil(total_amount_for_chips) + total_amount_for_beer

if total_spend <= budget:
    money_left = budget - total_spend
    print(f"{fan_name} bought a snack and has {money_left:.2f} leva left.")
else:
    money_needed = total_spend - budget
    print(f"{fan_name} needs {money_needed:.2f} more leva!")

