day_of_the_week = input()
price_of_ticket = 0

if day_of_the_week == "Monday":
    price_of_ticket = 12
elif day_of_the_week == "Tuesday":
    price_of_ticket = 12
elif day_of_the_week == "Wednesday":
    price_of_ticket = 14
elif day_of_the_week == "Thursday":
    price_of_ticket = 14
elif day_of_the_week == "Friday":
    price_of_ticket = 12
elif day_of_the_week == "Saturday":
    price_of_ticket = 16
elif day_of_the_week == "Sunday":
    price_of_ticket = 16

print(price_of_ticket)
