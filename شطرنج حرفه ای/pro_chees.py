n = input()

n1,n2,n3,n4,n5,n6 = n.split(" ")
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
n4 = int(n4)
n5 = int(n5)
n6 = int(n6)

if n1 != 1 :
    n1 = 1 - n1
else :
    n1 = 0

if n2 != 1 :
    n2 = 1 - n2
else :
    n2 = 0

if n3 != 2 :
    n3 = 2 - n3
else :
    n3 = 0

if n4 != 2 :
    n4 = 2 - n4
else :
    n4 = 0

if n5 != 2 :
    n5 = 2 - n5
else :
    n5 = 0

if n6 != 8 :
    n6 = 8 - n6
else :
    n6 = 0

print(n1,n2,n3,n4,n5,n6)