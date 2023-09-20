days_staying = int(input())
room_type = input()
rating = input()
price_per_night = 0
nights_staying = days_staying - 1
discount = 0


if room_type == "room for one person":
    price_per_night = 18

elif room_type == "apartment":
    price_per_night = 25.00
    if nights_staying < 10:
        price_per_night *= 0.70
    elif nights_staying <= 15:
        price_per_night *= 0.65
    else:
        price_per_night *= 0.50


elif room_type == "president apartment":
    price_per_night = 35.00
    if nights_staying < 10:
        price_per_night *= 0.90
    elif nights_staying <= 15:
        price_per_night *= 0.85
    else:
        price_per_night *= 0.80

cost_of_staying = nights_staying * price_per_night

if rating == "positive":
    cost_of_staying *= 1.25
elif rating == "negative":
    cost_of_staying *= 0.90

print(f"{cost_of_staying:.2f}")

