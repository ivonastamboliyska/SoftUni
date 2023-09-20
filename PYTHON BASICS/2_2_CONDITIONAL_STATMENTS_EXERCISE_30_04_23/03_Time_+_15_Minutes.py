hours = int(input())
minutes = int(input())

hours_as_minutes = hours * 60
total_minutes = hours_as_minutes + minutes
additional_minutes = 15
clock_showing = total_minutes + additional_minutes

hours_showing = clock_showing // 60
minutes_showing = clock_showing % 60
if minutes_showing > 59:
    hours_showing += 1
if hours_showing == 24:
    hours_showing = 00

print(f"{hours_showing}:{minutes_showing:02d}")