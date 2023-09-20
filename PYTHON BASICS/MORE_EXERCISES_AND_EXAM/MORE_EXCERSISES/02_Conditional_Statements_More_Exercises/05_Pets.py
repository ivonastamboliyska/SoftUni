import math

days_count = int(input())
food_in_kg = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day = float(input())

total_dog_food = days_count * dog_food_per_day
total_cat_food = days_count * cat_food_per_day
total_turtle_food = days_count * (turtle_food_per_day / 1000)

eaten_food = total_dog_food + total_cat_food + total_turtle_food

if eaten_food <= food_in_kg:
    excess_food = food_in_kg - eaten_food
    print(f"{int(excess_food)} kilos of food left.")
else:
    insufficient_food = food_in_kg - eaten_food
    # math.ceil(insufficient_food)
    print(f"{math.ceil( - insufficient_food)} more kilos of food are needed.")