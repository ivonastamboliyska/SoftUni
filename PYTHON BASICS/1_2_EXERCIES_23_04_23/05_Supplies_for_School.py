PENS_PRICE = 5.80
MARKERS_PRICE = 7.20
CLEANING_DETERGENT = 1.20

pens_qty = int(input())
markers_qty = int(input())
cleaning_detergent = int(input())
discount = int(input()) / 100

total_amount = PENS_PRICE * pens_qty \
               + MARKERS_PRICE * markers_qty \
               + CLEANING_DETERGENT * cleaning_detergent
price_with_discount = total_amount - (total_amount * discount)

print(price_with_discount)