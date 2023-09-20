
# След това n – на брой пъти се чете име на уебсайт – текст

FACEBOOK_FINE = 150
INSTAGRAM_FINE = 100
REDDIT_FINE = 50

tabs_opened = int(input())
salary = float(input())

for tab in range(tabs_opened):
    current_tab = input()
    if current_tab == "Facebook":
        salary -= FACEBOOK_FINE
    elif current_tab == "Instagram":
        salary -= INSTAGRAM_FINE
    elif current_tab == "Reddit":
        salary -= REDDIT_FINE
    if salary <= 0:
        break

if salary > 0:
    print(f"{int(salary)}")
else:
    print(f"You have lost your salary.")

