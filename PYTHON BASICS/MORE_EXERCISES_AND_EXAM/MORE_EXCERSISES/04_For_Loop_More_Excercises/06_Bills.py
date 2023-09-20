months = int(input())
electricity_bill = 0
water_bill = 0
internet_bill = 0
other_bills = 0

for i in range(months):
    electricity_bill += float(input())
    water_bill += 20
    internet_bill += 15


other_bills = electricity_bill + water_bill + internet_bill + (electricity_bill + water_bill + internet_bill) * 0.20
average_bill = (electricity_bill + water_bill + internet_bill + other_bills) / months

print(f"Electricity: {electricity_bill:.2f} lv")
print(f"Water: {water_bill:.2f} lv")
print(f"Internet: {internet_bill:.2f} lv")
print(f"Other: {other_bills:.2f} lv")
print(f"Average: {average_bill:.2f} lv")

