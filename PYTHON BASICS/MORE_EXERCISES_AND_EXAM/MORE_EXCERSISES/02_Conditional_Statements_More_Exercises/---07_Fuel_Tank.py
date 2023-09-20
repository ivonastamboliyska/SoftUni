fuel_type = input()
liters_fuel_in_tank = int(input())

if fuel_type == "Diesel" or "Gasoline" or "Gas":
    if liters_fuel_in_tank >= 25:
        print(f"You have enough {fuel_type.lower()}.")
    else:
        print(f"Fill your tank with {fuel_type.lower()}!")
else:
    print("Invalid fuel!")
