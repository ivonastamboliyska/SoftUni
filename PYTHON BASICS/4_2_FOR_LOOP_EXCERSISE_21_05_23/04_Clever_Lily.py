current_age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

money = 0
toy_count = 0

for birthday in range(1, current_age + 1):
    if birthday % 2 == 0:
        money += birthday * 10 / 2
        money -= 1
    else:
        toy_count += 1


money += toy_count * toy_price

if money >= washing_machine_price:
    money_left = money - washing_machine_price
    print(f"Yes! {money_left:.2f}")
else:
    difference = washing_machine_price - money
    print(f"No! {difference:.2f}")