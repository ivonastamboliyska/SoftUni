# От конзолата се четат точно 3 числа, всяко на отделен ред:
# N – цяло число – 0 <= N < M
# M – цяло число – N < M <= 10000
# S – цяло числo – N <= S <= M

n_address = int(input())
m_address = int(input())
s_address = int(input())

for number in range(m_address + 1, n_address - 1, -1):
    if number % 2 == 0 and number % 3 == 0:
        if number == s_address:
            break
    if number % 2 == 0 and number % 3 == 0:
        print(number, end=" ")
