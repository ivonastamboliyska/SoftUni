# for i in range(7+1):
#     for j in range(i):
#         print(i, end='')
#     print('')

number = int(input())

for i in range(1, number + 1):
    for j in range(0, i):
        print('*', end='')
    print('')
for i in range(number -1, 0, -1):
    for j in range(0,i):
        print('*', end='')
    print('')