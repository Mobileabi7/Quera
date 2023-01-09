str1 = input ()
str2 = input()
lst1 = []
lst2 = []
for i in str1 :
    lst1.append(i)
for j in str2 :
    lst2.append(j)

if lst1[0] == lst2[-1] :
    print("YES")
else :
    print('NO')
