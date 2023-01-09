# لوزی های ستاره ای
# https://b2n.ir/y21327

n = int(input())

for i in range(1, n + 1, 2):
    print(f'{" " * ((n - i) // 2)}{"*" * i}{" " * (n - i - 1)}{"*" * i}')
for i in range(n - 2, 0, -2):
    print(f'{" " * ((n - i) // 2)}{"*" * i}{" " * (n - i - 1)}{"*" * i}')

###########################################################

n = int(input())
i = n // 2
for j in range(n):
    print(abs(i) * ' ' + (n - 2 * abs(i)) * '*' + abs(i) * ' ', end='')
    print(abs(i) * ' ' + (n - 2 * abs(i)) * '*' + abs(i) * ' ')
    i -= 1