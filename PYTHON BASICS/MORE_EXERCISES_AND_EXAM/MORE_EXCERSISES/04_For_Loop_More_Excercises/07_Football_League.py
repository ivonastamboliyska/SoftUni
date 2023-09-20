stadium_capacity = int(input())
fans = int(input())
sector_a_count = 0
sector_b_count = 0
sector_v_count = 0
sector_g_count = 0


for i in range(fans):
    sector = input()
    if sector == "A":
        sector_a_count += 1
    elif sector == "B":
        sector_b_count += 1
    elif sector == "V":
        sector_v_count += 1
    elif sector == "G":
        sector_g_count += 1

percent_sector_a = sector_a_count / fans * 100
percent_sector_b = sector_b_count / fans * 100
percent_sector_v = sector_v_count / fans * 100
percent_sector_g = sector_g_count / fans * 100
percent_of_fans = fans/stadium_capacity * 100

print(f"{percent_sector_a:.2f}%")
print(f"{percent_sector_b:.2f}%")
print(f"{percent_sector_v:.2f}%")
print(f"{percent_sector_g:.2f}%")
print(f"{percent_of_fans:.2f}%")