# Входът се чете от конзолата и съдържа точно 2 реда:
# •	Наследените пари – реално число в интервала [1.00 ... 1 000 000.00]
# •	Годината, до която трябва да живее (включително) – цяло число в интервала [1801 ... 1900]

inherited_money = float(input())
year_he_has_to_live = int(input())
money_spend = 0
current_years = 18

for year in range(1800, year_he_has_to_live + 1):
    if year % 2 == 0:
        money_spend += 12000
        current_years += 1
    elif year % 2 != 0:
        money_spend += 12000 + 50 * current_years
        current_years += 1

if money_spend <= inherited_money:
    money_left = inherited_money - money_spend
    print(f"Yes! He will live a carefree life and will have {money_left:.2f} dollars left.")
else:
    money_needed = money_spend - inherited_money
    print(f"He will need {money_needed:.2f} dollars to survive.")
