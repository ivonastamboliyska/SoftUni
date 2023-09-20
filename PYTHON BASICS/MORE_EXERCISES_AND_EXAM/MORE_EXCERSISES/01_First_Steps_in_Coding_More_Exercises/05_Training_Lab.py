length_in_meters = float(input())
width_in_meters = float(input())

working_places_not_available = 3

working_place_length = 120
working_place_width = 70
hall_size = 100

length_in_cm = length_in_meters * 100
width_in_cm = (width_in_meters * 100) - hall_size


working_place_per_column = length_in_cm // working_place_length
working_places_per_row = width_in_cm // working_place_width
total_working_places = (working_places_per_row * working_place_per_column) - working_places_not_available

print(total_working_places)



