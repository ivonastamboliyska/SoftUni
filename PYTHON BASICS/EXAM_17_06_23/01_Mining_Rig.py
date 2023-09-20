from math import ceil
video_card_price = int(input())
transition_price = int(input())
electricity_per_card_per_day = float(input())
income_per_card_per_day = float(input())

video_card_count = 13
transition_count = 13
other_components_price = 1000

total_price_video_card = video_card_price * video_card_count
total_transition_price = transition_price * transition_count

total_price_for_components = total_price_video_card + total_transition_price + other_components_price

income_from_video_card_per_day = income_per_card_per_day - electricity_per_card_per_day
total_income = video_card_count * income_from_video_card_per_day

investment_return_in_days = total_price_for_components / total_income

print(total_price_for_components)
print(ceil(investment_return_in_days))
