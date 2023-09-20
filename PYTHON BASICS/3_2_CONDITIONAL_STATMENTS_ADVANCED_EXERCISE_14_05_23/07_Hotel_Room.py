month = input()
nights_count = int(input())
discount = 0
studio_price_per_night = 0
apartment_price_per_night = 0

if month == "May" or month == "October":
    studio_price_per_night = 50
    if 7 < nights_count < 14:
        studio_price_per_night *= 0.95
    elif nights_count > 14:
        studio_price_per_night *= 0.70
    apartment_price_per_night = 65
    if nights_count > 14:
        apartment_price_per_night *= 0.90
if month == "June" or month == "September":
    studio_price_per_night = 75.20
    if nights_count > 14:
        studio_price_per_night *= 0.80
    apartment_price_per_night = 68.70
    if nights_count > 14:
        apartment_price_per_night *= 0.90
if month == "July" or month == "August":
    studio_price_per_night = 76
    apartment_price_per_night = 77
    if nights_count > 14:
        apartment_price_per_night *= 0.90

price_for_the_apartment_stay = nights_count * apartment_price_per_night
price_for_the_studio_stay = nights_count * studio_price_per_night
# Да се отпечатат на конзолата 2 реда:
# ⦁	На първия ред: "Apartment: {цена за целият престой} lv."
# ⦁	На втория ред: "Studio: {цена за целият престой} lv."
# Цената за целия престой да е форматирана с точност до два знака след десетичната запетая.

print(f"Apartment: {price_for_the_apartment_stay:.2f} lv.")
print(f"Studio: {price_for_the_studio_stay:.2f} lv.")
