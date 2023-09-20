days_count = 0
money_spending_count = 0

money_needed = float(input())
money_available = float(input())

while money_available < money_needed and money_spending_count < 5:
    command = input()
    money = float(input())
    days_count += 1

    if command == "save":
        money_available += money
        money_spending_count = 0
    elif command == "spend":
        money_available -= money
        money_spending_count += 1
        if money_available < 0:
            money_available = 0

if money_spending_count == 5:
    print("You can't save the money.")
    print(days_count)

if money_available >= money_needed:
    print(f"You saved the money for {days_count} days.")
