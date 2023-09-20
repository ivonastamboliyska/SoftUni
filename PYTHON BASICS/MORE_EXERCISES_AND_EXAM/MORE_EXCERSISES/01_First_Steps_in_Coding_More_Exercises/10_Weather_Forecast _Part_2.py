temperature = float(input())

if 26 <= temperature <= 35:
    print("Hot")
elif 20 < temperature < 26:
    print("Warm")
elif 15 <= temperature <= 20:
    print("Mild")
elif 12 <= temperature < 15:
    print("Cool")
elif 5 <= temperature < 12:
    print("Cold")
else:
    print("unknown")