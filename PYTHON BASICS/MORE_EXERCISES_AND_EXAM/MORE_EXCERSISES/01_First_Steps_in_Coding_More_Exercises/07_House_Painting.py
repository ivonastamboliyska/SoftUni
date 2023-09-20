house_height = float(input())
side_wall_length = float(input())
triangle_wall_height = float(input())

liter_green_paint_per_square_meter = 3.4
liter_red_paint_per_square_meter = 4.3

door_area = 1.2 * 2
window_area = 1.5 * 1.5

front_wall_area = (house_height * house_height) - door_area
back_wall_area = house_height * house_height
side_wall_area = (house_height * side_wall_length) - window_area  #2

side_roof_wall_area = house_height * side_wall_length  #2
front_roof_wall_area = house_height * triangle_wall_height / 2
back_roof_wall_area = house_height * triangle_wall_height / 2

total_house_area = front_wall_area + back_wall_area + side_wall_area * 2
total_roof_area = side_roof_wall_area * 2 + front_roof_wall_area + back_roof_wall_area

total_green_paint = total_house_area / liter_green_paint_per_square_meter
total_red_paint = total_roof_area / liter_red_paint_per_square_meter

print(f"{total_green_paint:.2f}")
print(f"{total_red_paint:.2f}")


# Покривът има следните размери:
# •	Два правоъгълника със страни „x“ и „y“
# •	Два равностранни триъгълника със страна „x“ и височина „h“
# Трябва да пресметнете площта на всички страни и площта на покрива, за да
# намерите колко литра от всяка боя ще са нужни.


