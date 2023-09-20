NYLON_PRICE = 1.50
PAINT_PRICE = 14.50
PAINT_THINNER_PRICE = 5.00
BAG_PRICE = 0.40

nylon_qty = int(input())
paint_qty = int(input())
paint_thinner_qty = int(input())
hours_needed = int(input())

extra_nylon = 2
extra_paint = 0.10 * paint_qty

amount_materials = (nylon_qty + extra_nylon) * NYLON_PRICE \
                   + (paint_qty + extra_paint) * PAINT_PRICE \
                   + paint_thinner_qty * PAINT_THINNER_PRICE \
                   + BAG_PRICE

works_per_hour_price = amount_materials * 0.30
total_amount = amount_materials + works_per_hour_price * hours_needed

print(total_amount)
