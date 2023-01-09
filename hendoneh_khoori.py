#هندونه خوری 
#https://quera.org/problemset/35253/

n = int(input())

lst = []
for i in input().split():
    lst.append(int(i))
# string = [int(i) for i in input().split()]
print(lst.index(max(lst)) + 1)



