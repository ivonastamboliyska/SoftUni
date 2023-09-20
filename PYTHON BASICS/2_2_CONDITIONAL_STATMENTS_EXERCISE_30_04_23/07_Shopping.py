VIDEOCARD_PRICE = 250

budget = float(input())
videocard_bought = int(input())
processor_bought = int(input())
ram_bought = int(input())

amount_for_video_card = videocard_bought * VIDEOCARD_PRICE
processor_price = amount_for_video_card * 0.35
ram_price = amount_for_video_card * 0.10

total_amount = videocard_bought * VIDEOCARD_PRICE\
               + processor_bought * processor_price\
               + ram_bought * ram_price
discount = 0
if videocard_bought > processor_bought:
    discount = 0.15

total_amount_with_discount = total_amount * (1 - discount)
money_left = budget - total_amount_with_discount
money_needed = total_amount_with_discount - budget

if budget >= total_amount:
    print(f"You have {money_left:.2f} leva left!")
else:
    print(f"Not enough money! You need {money_needed:.2f} leva more!")

