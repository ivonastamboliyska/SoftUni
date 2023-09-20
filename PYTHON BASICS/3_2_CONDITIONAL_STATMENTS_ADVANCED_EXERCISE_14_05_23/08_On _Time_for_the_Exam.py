
exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_time_in_min = exam_hour * 60 + exam_minutes
arrival_time_in_min = arrival_hour * 60 + arrival_minutes
difference = arrival_time_in_min - exam_time_in_min

if difference > 0:
    print("Late")
    if difference < 60:
        print(f"{difference} minutes after the start")
    else:
        hh = abs(difference) // 60
        mm = abs(difference) % 60
        print(f"{hh}:{mm:02d} hours after the start")

elif difference >= -30:
    print("On time")
    if not difference == 0:
        mm = abs(difference) % 60
        print(f"{mm} minutes before the start")

else:
    print("Early")
    if difference > -60:
        print(f"{abs(difference)} minutes before the start")
    else:
        hh = abs(difference) // 60
        mm = abs(difference) % 60
        print(f"{hh}:{mm :02d} hours before the start")