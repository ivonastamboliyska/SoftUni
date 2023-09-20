CHICKEN_MENU_PRICE = 10.35
FISH_MENU_PRICE = 12.40
VEGETARIAN_MENU_PRICE = 8.15
DELIVERY_PRICE = 2.50

chicken_menu_qty = int(input())
fish_menu_qty = int(input())
vegetarian_menu_qty = int(input())

dessert_price = (chicken_menu_qty * CHICKEN_MENU_PRICE\
                + fish_menu_qty * FISH_MENU_PRICE\
                + vegetarian_menu_qty * VEGETARIAN_MENU_PRICE) * 0.20

order_total_amount = dessert_price + chicken_menu_qty * CHICKEN_MENU_PRICE\
                + fish_menu_qty * FISH_MENU_PRICE\
                + vegetarian_menu_qty * VEGETARIAN_MENU_PRICE + DELIVERY_PRICE

print(order_total_amount)

