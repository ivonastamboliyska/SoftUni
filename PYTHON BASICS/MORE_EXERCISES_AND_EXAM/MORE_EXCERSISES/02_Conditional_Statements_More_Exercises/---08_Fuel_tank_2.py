fuel_type = input()
fuel_quantity = float(input())
club_card = input()

gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93

if fuel_type == "Gasoline":
    price_of_fuel = fuel_quantity * gasoline_price
    if club_card == "Yes":
        discount_club_card_per_liter = 0.18
        discounted_price = gasoline_price - discount_club_card_per_liter
        total_price_of_fuel = price_of_fuel - discounted_price
    if 20 <= fuel_quantity <= 25:
        additional_discount = 0.08
    elif fuel_quantity > 25:
        additional_discount = 0.10

if fuel_type == "Diesel":
    price_of_fuel = fuel_quantity * diesel_price
    if club_card == "Yes":
        discount_club_card_per_liter = 0.12
        discounted_price = diesel_price - discount_club_card_per_liter
        total_price_of_fuel = price_of_fuel - discounted_price
    if 20 <= fuel_quantity <= 25:
        additional_discount = 0.08
    elif fuel_quantity > 25:
        additional_discount = 0.10

if fuel_type == "Gas":
    price_of_fuel = fuel_quantity * gas_price
    if club_card == "Yes":
        discount_club_card_per_liter = 0.08
        discounted_price = gas_price - discount_club_card_per_liter
        total_price_of_fuel = discounted_price * fuel_quantity
    if 20 <= fuel_quantity <= 25:
        additional_discount = 0.08
    elif fuel_quantity > 25:
        additional_discount = 0.10



print(f"{price_of_fuel:.2f} lv.")


