from math import ceil

magnolia_count = int(input())
hyacinth_count = int(input())
rose_count = int(input())
cactus_count = int(input())
price_of_present = float(input())

magnolia_price = 3.25
hyacinth_price = 4
rose_price = 3.50
cactus_price = 8

total_flowers_price = magnolia_price * magnolia_count \
                       + hyacinth_price * hyacinth_count \
                       + rose_price * rose_count \
                       + cactus_price * cactus_count
taxes = total_flowers_price * 0.05
income = total_flowers_price - taxes

if income >= price_of_present:
    money_left = income - price_of_present
    print(f"She is left with {int(money_left)} leva.")

else:
    money_needed = price_of_present - income

    print(f"She will have to borrow {ceil(money_needed)} leva.")



