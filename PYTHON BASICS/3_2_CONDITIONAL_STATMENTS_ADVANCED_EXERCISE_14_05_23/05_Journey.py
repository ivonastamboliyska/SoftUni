budget = float(input())
season = input()
percentage_spent = 0
destination = 0
type_of_vacation = 0

if budget <= 100 and season == "summer":
    destination = "Bulgaria"
    type_of_vacation = "Camp"
    percentage_spent = 0.3
elif budget <= 100 and season == "winter":
    destination = "Bulgaria"
    type_of_vacation = "Hotel"
    percentage_spent = 0.7

if 100 < budget <= 1000 and season == "summer":
    destination = "Balkans"
    type_of_vacation = "Camp"
    percentage_spent = 0.4
elif 100 < budget <= 1000 and season == "winter":
    destination = "Balkans"
    type_of_vacation = "Hotel"
    percentage_spent = 0.8

if budget > 1000:
    destination = "Europe"
    type_of_vacation = "Camp" and "Hotel"
    percentage_spent = 0.9

amount_spent = budget * percentage_spent

print(f"Somewhere in {destination}")
print(f"{type_of_vacation} - {amount_spent:.2f}")
