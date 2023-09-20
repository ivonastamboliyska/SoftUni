distance_in_km = int(input())
time_of_the_day = input()
total_price = 0

if time_of_the_day == "day":
    if distance_in_km < 20:
        additional_tax = 0.70
        taxi_price_per_km = 0.79
        total_price = distance_in_km * taxi_price_per_km + additional_tax
    elif distance_in_km < 100:
        bus_price_per_km = 0.09
        total_price = distance_in_km * bus_price_per_km
    elif distance_in_km >= 100:
        train_price_per_km = 0.06
        total_price = distance_in_km * train_price_per_km


elif time_of_the_day == "night":
    if distance_in_km < 20:
        additional_tax = 0.70
        taxi_price_per_km = 0.90
        total_price = distance_in_km * taxi_price_per_km + additional_tax
    elif distance_in_km < 100:
        bus_price_per_km = 0.09
        total_price = distance_in_km * bus_price_per_km
    elif distance_in_km >= 100:
        train_price_per_km = 0.06
        total_price = distance_in_km * train_price_per_km

print(f"{total_price:.2f}")

