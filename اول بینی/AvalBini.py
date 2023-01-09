

n1 = int(input())
n2 = int(input())
lst = []
for number in range(n1+1,n2) :
    lst.append(number)


addAval = []
lst2 = []
for i in lst :
    counter = 0
    for j in range(1,i+1):
        if i % j == 0 :
            counter += 1
    if counter == 2 :
            addAval.append(i)
            counter == 0
# print((addAval))            
result =''
for i in addAval:
    result = result+str(i)+","
result = result[:-1]
print(result)


#............................................
# n1 = int(input('bazeh ebtedaeei : '))
# n2 = int(input('bazeh Entehaeei : '))
# lst = []
# for number in range(n1+1,n2) :
# addAval = []
# lst2 = []
# for i in lst :
#     counter = 0
#     # print('i :',i)
#     for j in range(1,i+1):
#         # print('j is :',j)
#         if i % j == 0 :
#             counter += 1
#             # print('counter : ',counter)
#     if counter == 2 :
#             addAval.append(i)
#             counter == 0
#             # print(addAval)
# print((addAval))