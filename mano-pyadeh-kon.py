n = int(input())
result = 0
for i in range(1 , n ):
    print('i is : ' ,i)
    for j in range(1 , i ):
        print('j is : ', j)
        result = result + 1
        print('result is ',result)
# print(result)