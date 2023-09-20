total_amount = 0
command = input()
while command != "NoMoreMoney":
    payment = float(command)
    if payment < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {payment:.2f}")
    total_amount += payment
    command = input()
print(f"Total: {total_amount:.2f}")
