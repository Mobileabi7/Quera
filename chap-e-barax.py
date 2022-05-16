n =''
lst =[]
while n != 0 :
    n= int(input())
    if n == 0 :
        break
    else :
        lst.append(n)
lst.reverse()
for i in lst:
    print(i)


