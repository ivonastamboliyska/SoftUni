# След това се чете по един ред до получаване на команда "Stop" или докато фирмата не продаде всички пакети:
# Име на пакет – текст с възможности "sea" или "mountain"

sea_vacations_count = int(input())
mountain_vacations_count = int(input())
sea_vacation_price = 680
mountain_vacation_price = 499
vacation = ""
profit = 0
all_packages_available = sea_vacations_count + mountain_vacations_count

while all_packages_available != 0:
    vacation = input()
    if vacation == "Stop":
        break

    if vacation == "sea":
        if sea_vacations_count == 0:
            continue
        sea_vacations_count -= 1
        profit += sea_vacation_price
        all_packages_available -= 1


    elif vacation == "mountain":
        if mountain_vacations_count == 0:
            continue
        mountain_vacations_count -= 1
        profit += mountain_vacation_price
        all_packages_available -= 1

if sea_vacations_count == 0 and mountain_vacations_count == 0:
    print(" Good job! Everything is sold.")

print(f"Profit: {profit} leva.")
