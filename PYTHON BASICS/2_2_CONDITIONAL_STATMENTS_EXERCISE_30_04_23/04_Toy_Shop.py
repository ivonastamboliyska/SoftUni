PUZZLE_PRICE = 2.60
TALKING_DOLL_PRICE = 3.00
TEDDY_BEAR_PRICE = 4.10
MINION_PRICE = 8.20
TRUCK_PRICE = 2.00

vacation_price = float(input())
puzzle_ordered = int(input())
talking_doll_ordered = int(input())
teddy_bear_ordered = int(input())
minion_ordered = int(input())
truck_ordered = int(input())

total_price_of_order = puzzle_ordered * PUZZLE_PRICE \
                       + talking_doll_ordered * TALKING_DOLL_PRICE \
                       + teddy_bear_ordered * TEDDY_BEAR_PRICE \
                       + minion_ordered * MINION_PRICE \
                       + truck_ordered * TRUCK_PRICE

total_toys_ordered = puzzle_ordered \
                     + talking_doll_ordered \
                     + teddy_bear_ordered \
                     + minion_ordered \
                     + truck_ordered
discount = 0
if total_toys_ordered >= 50:
    discount = 0.25

income = total_price_of_order * (1 - discount)
rent_payment = income * 0.10

total_income = income - rent_payment

if total_income >= vacation_price:
    print(f"Yes! {total_income - vacation_price :.2f} lv left.")
else:
    print(f"Not enough money! {vacation_price - total_income :.2f} lv needed.")
