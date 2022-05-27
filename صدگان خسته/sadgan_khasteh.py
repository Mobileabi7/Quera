n1 = input()
n2 = input()

n1 = int(str(n1)[::-1])
n2 = int(str(n2)[::-1])

if n1>n2 :
    print(str(n2)[::-1],'<',str(n1)[::-1])
elif n1 == n2 :
    print(str(n2)[::-1],'=',str(n1)[::-1])
else :
    print(str(n1)[::-1],'<',str(n2)[::-1])
