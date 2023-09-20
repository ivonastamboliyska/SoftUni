price_of_the_party = float(input())
love_letters_count = int(input())
roses_count = int(input())
key_holders_count = int(input())
drawings_count = int(input())
lucky_surprises_count = int(input())

love_letters_price = 0.60
roses_price = 7.20
key_holders_price = 3.60
drawing_price = 18.20
lucky_surprise_price = 22

total_count_ordered = love_letters_count + roses_count + key_holders_count + drawings_count + lucky_surprises_count

total_amount_of_order = love_letters_count * love_letters_price \
               + roses_count * roses_price \
               + key_holders_count * key_holders_price \
               + drawings_count * drawing_price \
               + lucky_surprises_count * lucky_surprise_price

discount = 0
if total_count_ordered > 25:
    discount = 0.35 #35% diccount over 25 pcs

income = total_amount_of_order * (1 - discount)
hosting_fee = income * 0.10
total_income = income - hosting_fee

if total_income >= price_of_the_party:
    money_left = total_income - price_of_the_party
    print(f"Yes! {money_left:.2f} lv left.")
else:
    money_needed = price_of_the_party - total_income
    print(f"Not enough money! {money_needed:.2f} lv needed.")







# На конзолата се отпечатва:
# Ако парите са достатъчни се отпечатва:
# "Yes! {оставащите пари} lv left."
# Ако парите НЕ са достатъчни се отпечатва:
# "Not enough money! {недостигащите пари} lv needed."
# Резултатът трябва да се форматира до втория знак след десетичната запетая.




