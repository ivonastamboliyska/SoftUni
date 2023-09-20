budget = float(input())
statists_count = int(input())
costume_price_per_statist = float(input())

decor_price = budget * 0.10
costume_price = statists_count * costume_price_per_statist

discount = 0
if statists_count > 150:
    discount = 0.10

amount_for_clothes_and_decor = decor_price + costume_price * (1 - discount)
money_left = budget - amount_for_clothes_and_decor
money_needed = amount_for_clothes_and_decor - budget

if amount_for_clothes_and_decor > budget:
    print("Not enough money!")
    print(f"Wingard needs {money_needed:.2f} leva more.")
elif amount_for_clothes_and_decor <= budget:
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")
