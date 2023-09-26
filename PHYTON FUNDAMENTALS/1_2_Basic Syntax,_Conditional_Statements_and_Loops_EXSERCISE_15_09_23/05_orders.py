number_of_orders = int(input())
total_price = 0

for order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    # if
    price = price_per_capsule * capsules_per_day * days
    total_price += price
    print(f"{price:.2f}")
print(f"{total_price:.2f}")