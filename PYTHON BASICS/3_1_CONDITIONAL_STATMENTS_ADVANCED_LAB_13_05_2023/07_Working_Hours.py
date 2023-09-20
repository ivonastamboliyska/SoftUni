hour = int(input())
day_of_the_week = input()

if 10 <= hour <= 18:
    if day_of_the_week == "Monday":
        print("open")
    elif day_of_the_week == "Tuesday":
        print("open")
    elif day_of_the_week == "Wednesday":
        print("open")
    elif day_of_the_week == "Thursday":
        print("open")
    elif day_of_the_week == "Friday":
        print("open")
    elif day_of_the_week == "Saturday":
        print("open")
    elif day_of_the_week == "Sunday":
        print("closed")
else:
    print("closed")