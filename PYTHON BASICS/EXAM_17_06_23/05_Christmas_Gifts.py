command = input()
toys_count = 0
kids_count = 0
adults_count = 0
sweatshirts_count = 0
toy_price = 5
sweatshirts_price = 15
while command != "Christmas":
    age_of_family_member = int(command)
    command = input()
    if age_of_family_member <= 16:
        kids_count += 1
        toys_count += 1
    elif age_of_family_member > 16:
        adults_count += 1
        sweatshirts_count += 1

total_toys_price = kids_count * toy_price
total_sweatshirt_price = adults_count * sweatshirts_price


print(f"Number of adults: {adults_count}")
print(f"Number of kids: {kids_count}")
print(f"Money for toys: {total_toys_price}")
print(f"Money for sweaters: {total_sweatshirt_price}")