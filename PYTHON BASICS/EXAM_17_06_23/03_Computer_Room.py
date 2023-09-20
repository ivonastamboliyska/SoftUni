# Входът се чете от конзолата и съдържа точно 4 реда:
# На първия ред - месецът - текст с възможности: "march", "april", "may", "june", "july", "august"
# На втория ред - броят на прекараните часове - цяло число в диапазона [1...10]
# На третия ред - броят на хората в групата -  цяло число в диапазона [1...10]
# На четвъртия ред - времето от деня – текст с възможности: "day" или "night"

month = input()
hours_spend = int(input())
people_in_group = int(input())
time_of_the_day = input()
price_per_hour = 0

if month == "march" or month == "april" or month == "may":
    if time_of_the_day == "day":
        price_per_hour = 10.50
        if people_in_group >= 4:
            price_per_hour = price_per_hour * 0.90
            if hours_spend >= 5:
                price_per_hour = price_per_hour * 0.50
    elif time_of_the_day == "night":
        price_per_hour = 8.40
        if people_in_group >= 4:
            price_per_hour = price_per_hour * 0.90
            if hours_spend >= 5:
                price_per_hour = price_per_hour * 0.50

elif month == "june" or month == "july" or month == "august":
    if time_of_the_day == "day":
        price_per_hour = 12.60
        if people_in_group >= 4:
            price_per_hour = price_per_hour * 0.90
            if hours_spend >= 5:
                price_per_hour = price_per_hour * 0.50
    elif time_of_the_day == "night":
        price_per_hour = 10.20
        if people_in_group >= 4:
            price_per_hour = price_per_hour * 0.90
            if hours_spend >= 5:
                price_per_hour = price_per_hour * 0.50

total_price = price_per_hour * hours_spend * people_in_group


print(f"Price per person for one hour: {price_per_hour:.2f}")
print(f"Total cost of the visit: {total_price:.2f}")
