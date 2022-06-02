#ساده تر
# https://quera.org/problemset/3403/
from numpy import average


lst = []
for i in range (4) :
    n = int(input())
    lst.append(n)
print('Sum :',"%.6f"%sum(lst))
print('Average :',"%.6f"%average(lst))
print('Product :',"%.6f"%(lst[0]*lst[1]*lst[2]*lst[3]))
print('MAX :',"%.6f"%max(lst))
print('MIN :',"%.6f"%min(lst))