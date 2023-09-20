musala_count = 0
montblanc_count = 0
kilimanjaro_count = 0
k2_count = 0
everest_count = 0

group_count = int(input())
people_in_group = 0

for _ in range(group_count):
    people_in_group = int(input())

    if people_in_group <= 5:
        musala_count += people_in_group
    elif people_in_group <= 12:
        montblanc_count += people_in_group
    elif people_in_group <= 25:
        kilimanjaro_count += people_in_group
    elif people_in_group <= 40:
        k2_count += people_in_group
    elif people_in_group > 40:
        everest_count += people_in_group

total_climbers = musala_count + montblanc_count + kilimanjaro_count + k2_count + everest_count

musala_percent = musala_count / total_climbers * 100
montblanc_percent = montblanc_count / total_climbers * 100
kilimanjaro_percent = kilimanjaro_count / total_climbers * 100
k2_percent = k2_count / total_climbers * 100
everest_percent = everest_count / total_climbers * 100
