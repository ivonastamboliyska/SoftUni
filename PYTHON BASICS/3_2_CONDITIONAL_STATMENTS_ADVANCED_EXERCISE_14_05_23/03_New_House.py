
flower_type = input()
flower_pcs = int(input())
budget = int(input())

price_roses = 5
price_dahlias = 3.80
price_tulips = 2.80
price_narcissus = 3.00
price_gladiolus = 2.50

price = 0
discount = 0


if flower_type == "Roses":
    price = price_roses
    if flower_pcs > 80:
        discount = 0.10
elif flower_type == "Dahlias":
    price = price_dahlias
    if flower_pcs > 90:
        discount = 0.15
elif flower_type == "Tulips":
    price = price_tulips
    if flower_pcs > 80:
        discount = 0.15
elif flower_type == "Narcissus":
    price = price_narcissus
    if flower_pcs < 120:
        discount = -0.15
elif flower_type == "Gladiolus":
    price = price_gladiolus
    if flower_pcs < 80:
        discount = -0.20

final_price = flower_pcs * price * (1 - discount)

if budget >= final_price:
    print(f"Hey, you have a great garden with {flower_pcs} {flower_type} and {budget - final_price:.2f} leva left.")
else:
    print(f"Not enough money, you need {final_price - budget:.2f} leva more.")