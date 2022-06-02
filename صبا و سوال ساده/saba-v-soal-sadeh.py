#صبا و سوال ساده
# https://quera.org/problemset/31025/
import math
n = int(input())
k = int(input())
while k != 0 :
    n = n/2
    k = k-1
print(math.floor(n))


