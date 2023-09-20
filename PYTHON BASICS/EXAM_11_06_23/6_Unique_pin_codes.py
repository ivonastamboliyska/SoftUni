upper_limit_first_number = int(input())
upper_limit_second_number = int(input())
upper_limit_third_number = int(input())

for x1 in range(1, upper_limit_first_number + 1):
    if x1 % 2 != 0:
        break
    elif x1 % 2 == 0:
        print(x1)
    for x2 in range(1, upper_limit_second_number + 1):
        if x2 / x2 != 0:
            break
        elif x2 / x2 == 0:
            print(x2)
        for x3 in range(1,upper_limit_third_number + 1):
            if x3 % 2 != 0:
                break
            elif x3 % 2 == 0:
                print(x3)
