import numpy as np

s = input()
a, b = s.split(" ")
a = float(a)
b = float(b)
lst = []

minus = np.arange(1, 100, 0.5).tolist()

for i in minus :
    x = i
    y = a-i
    z = b
    if (x+y) > z and (x+z) > y and (y+z) > x :
        lst.append("YES")

for j in minus :
    x = j
    y = b-j
    z = a
    if (x+y) > z and (x+z) > y and (y+z) > x :
        lst.append("YES")

if len(lst) == 0:
    print("NO")
else :
    print("YES")



