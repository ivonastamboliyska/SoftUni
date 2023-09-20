vineyard_area = int(input())
grape_kg_per_square_meter = float(input())
wine_needed = int(input())
staff_count = int(input())

area_for_wine = 0.4             # 40%
grape_needed_per_liter_wine = 2.5

grape_for_wine_harvested = vineyard_area * area_for_wine
total_grape_for_wine = grape_for_wine_harvested * grape_kg_per_square_meter

liters_wine_produced = total_grape_for_wine / grape_needed_per_liter_wine

if liters_wine_produced < wine_needed:
    insufficient_wine = wine_needed - liters_wine_produced
    print(f"It will be a tough winter! More {int(insufficient_wine):.0f} liters wine needed.")

else:
    excess_wine = liters_wine_produced - wine_needed
    print(f"Good harvest this year! Total wine: {int(liters_wine_produced):.0f} liters.")
    wine_per_person = excess_wine / staff_count
    print(f"{excess_wine:.0f} liters left -> {wine_per_person:.0f} liters per person. ")
