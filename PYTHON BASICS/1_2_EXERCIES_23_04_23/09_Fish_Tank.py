length = int(input())
width = int(input())
height = int(input())
obstacles = float(input())

total_volume = (length * width * height) / 1000
water_needed = total_volume * (1 -obstacles / 100 )

print(water_needed)
