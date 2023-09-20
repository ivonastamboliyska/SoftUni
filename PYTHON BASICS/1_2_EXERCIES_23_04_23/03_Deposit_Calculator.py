deposit = float(input())
months = int(input())
interest = float(input()) / 100

amount = deposit + months * ((deposit * interest) / 12 )
print(amount)