bgn_vegetables_price_per_kg = float(input())
bgn_fruits_price_per_kg = float(input())
total_kg_vegetables = int(input())
total_kg_fruits = int(input())
EUR = 1.94

income_vegetables = bgn_vegetables_price_per_kg * total_kg_vegetables
income_fruits = bgn_fruits_price_per_kg * total_kg_fruits
bgn_to_eur_vegetables = income_vegetables / EUR
bgn_to_eur_fruits = income_fruits / EUR

eur_total_income = bgn_to_eur_fruits + bgn_to_eur_vegetables
print(f"{eur_total_income:.2f}")
