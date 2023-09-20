# Тегло на пратката в килограми – реално число в интервала [0.01 ... 150.00]
# Тип услуга –  текст със следните възможности: "standard" или "express"
# Разстояние в километри – цяло число в интервала [1 ... 1000]

weight_of_parcel = float(input())
type_of_service = input()
distance_in_km = float(input())
price_for_km = 0
markup = 0
total_cost_for_delivery = 0

if type_of_service == "standard":
    if weight_of_parcel < 1:
        price_for_km = 0.03
    elif 1 <= weight_of_parcel < 10:
        price_for_km = 0.05
    elif 10 <= weight_of_parcel < 40:
        price_for_km = 0.10
    elif 40 <= weight_of_parcel < 90:
        price_for_km = 0.15
    elif 90 <= weight_of_parcel < 150:
        price_for_km = 0.20

if type_of_service == "express":
    if weight_of_parcel < 1:
        price_for_km = 0.03
        markup = 0.80
    elif 1 <= weight_of_parcel < 10:
        price_for_km = 0.05
        markup = 0.40
    elif 10 <= weight_of_parcel < 40:
        price_for_km = 0.10
        markup = 0.05
    elif 40 <= weight_of_parcel < 90:
        price_for_km = 0.15
        markup = 0.02
    elif 90 <= weight_of_parcel < 150:
        price_for_km = 0.20
        markup = 0.01

total_markup = price_for_km * markup
cost_per_km = total_markup * weight_of_parcel
cost_of_delivery = cost_per_km * distance_in_km
total_cost_for_delivery = distance_in_km * price_for_km + cost_of_delivery


print(f"The delivery of your shipment with weight of {weight_of_parcel:.3f} kg. would cost {total_cost_for_delivery:.2f} lv.")


# Напишете програма, която да пресмята при зададено разстояние в км. ,
# тегло на пратката и вида услуга, каква ще бъде стойността за доставка на дадена пратка.
#
#
# Да се отпечата на конзолата един ред:
# "The delivery of your shipment with weight of {тегло} kg. would cost {цена} lv."
#
# Теглото да бъде закръглено до третия знак след десетичната запетая
# Цената да бъде закръглена до втория знак след десетичната запетая
