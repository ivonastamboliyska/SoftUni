price_of_fish_1 = float(input())         #скумрия
price_of_fish_2 = float(input())        #цаца
kg_of_fish_3 = float(input())       #паламуд
kg_of_fish_4 = float(input())       #сафрид
kg_mussels = int(input())

price_of_fish_3 = price_of_fish_1 + (price_of_fish_1 * 60) / 100
price_of_fish_4 = price_of_fish_2 + (price_of_fish_2 * 80) / 100
price_of_mussels = 7.50

money_needed = price_of_fish_3 * kg_of_fish_3 \
               + price_of_fish_4 * kg_of_fish_4 \
               + price_of_mussels * kg_mussels

print(f"{money_needed:.2f}")