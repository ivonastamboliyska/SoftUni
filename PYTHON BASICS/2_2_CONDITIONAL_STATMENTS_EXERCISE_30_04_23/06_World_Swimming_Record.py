from math import floor
RESISTANCE_IN_SECONDS = 12.5
RESISTANCE_IN_DISTANCE = 15
record_to_be_beaten = float(input())
distance_in_meters = float(input())
seconds_per_meter = float(input())

swimming_time = distance_in_meters * seconds_per_meter
resistance = (distance_in_meters // RESISTANCE_IN_DISTANCE) * RESISTANCE_IN_SECONDS
total_swimming_time = swimming_time + resistance
difference = total_swimming_time - record_to_be_beaten
times_resistance_will_appear = distance_in_meters // RESISTANCE_IN_DISTANCE
floor(times_resistance_will_appear)

if total_swimming_time < record_to_be_beaten:
    print(f"Yes, he succeeded! The new world record is {total_swimming_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {difference:.2f} seconds slower.")
