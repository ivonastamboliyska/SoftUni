cargo_count = int(input())
total_price = 0
total_tons = 0
tons_with_bus = 0
tons_with_truck = 0
tons_with_train = 0

for type_of_cargo in range(cargo_count):
    tons_of_cargo = int(input())
    if tons_of_cargo <= 3:
        price_per_ton_bus = 200
        total_price += price_per_ton_bus * tons_of_cargo
        total_tons += tons_of_cargo
        tons_with_bus += tons_of_cargo
    elif tons_of_cargo <= 11:
        price_per_ton_truck = 175
        total_price += price_per_ton_truck * tons_of_cargo
        total_tons += tons_of_cargo
        tons_with_truck += tons_of_cargo
    elif tons_of_cargo >= 12:
        price_per_ton_train = 120
        total_price += price_per_ton_train * tons_of_cargo
        total_tons += tons_of_cargo
        tons_with_train += tons_of_cargo

average_price_per_ton = total_price / total_tons
percent_per_bus = tons_with_bus / total_tons * 100
percent_per_truck = tons_with_truck / total_tons * 100
percent_per_train = tons_with_train / total_tons * 100

print(f"{average_price_per_ton:.2f}")
print(f"{percent_per_bus:.2f}%")
print(f"{percent_per_truck:.2f}%")
print(f"{percent_per_train:.2f}%")


# •	Втори ред – процентът тона превозвани с микробус (процент между 0.00% и 100.00%);
# •	Трети ред – процентът  тона превозвани с камион (процент между 0.00% и 100.00%);
# •	Четвърти ред – процентът тона превозвани с влак (процент между 0.00% и 100.00%).
