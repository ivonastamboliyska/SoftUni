pages = int(input())
pages_per_hour = int(input())
days = int(input())
hours = pages / pages_per_hour
total_days_needed = hours / days


print(int(total_days_needed))

