processor_price_in_dollars = float(input())
video_card_price_in_dollars = float(input())
ram_price_in_dollars = float(input())
ram_count = int(input())
discount = float(input()) * 100
usd_to_bgn = 1.57


processor_price_in_bgn = processor_price_in_dollars * usd_to_bgn
video_card_price_in_bgn = video_card_price_in_dollars * usd_to_bgn
ram_price_in_bgn = ram_price_in_dollars * usd_to_bgn

discounted_processor = processor_price_in_bgn - (processor_price_in_bgn * discount / 100)
discounted_video_card = video_card_price_in_bgn - (video_card_price_in_bgn * discount / 100)
total_price_for_ram = ram_price_in_bgn * ram_count

total_amount = discounted_processor + discounted_video_card + total_price_for_ram

print(f"Money needed - {total_amount:.2f} leva.")

# Да се отпечата на конзолата на един ред:
# •   Колко общо лева ще му трябват, за да си закупи частите.
#    "Money needed - {общо лева} leva."
# Сумата трябва да се форматира до втория знак след десетичната запетая.
