budget = int(input())
season = input()
fisher_count = int(input())
rent = 0
discount = 0
additional_discount = 0

if season == "Spring":
    rent = 3000
    if fisher_count <= 6:
        discount = 0.10
    elif 7 <= fisher_count <= 11:
        discount = 0.15
    elif fisher_count >= 12:
        discount = 0.25
if season == "Summer":
    rent = 4200
    if fisher_count <= 6:
        discount = 0.10
    elif 7 <= fisher_count <= 11:
        discount = 0.15
    elif fisher_count >= 12:
        discount = 0.25
if season == "Autumn":
    rent = 4200
    if fisher_count <= 6:
        discount = 0.10
    elif 7 <= fisher_count <= 11:
        discount = 0.15
    elif fisher_count >= 12:
        discount = 0.25
if season == "Winter":
    rent = 2600
    if fisher_count <= 6:
        discount = 0.10
    elif 7 <= fisher_count <= 11:
        discount = 0.15
    elif fisher_count >= 12:
        discount = 0.25

rent_with_discount = rent * (1 - discount)

if fisher_count % 2 == 0 and season != "Autumn":
    additional_discount = rent_with_discount * 0.05
else:
    additional_discount = 0

total_amount = rent_with_discount - additional_discount
money_left = budget - total_amount
money_needed = total_amount - budget
if budget >= total_amount:
    print(f"Yes! You have {money_left:.2f} leva left.")
elif budget < total_amount:
    print(f"Not enough money! You need {money_needed:.2f} leva.")
