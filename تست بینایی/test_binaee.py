n = int(input())
s = input()
e = input()
c = 0 


for i in range(n):
    if s[i] != e[i]:
        c += 1
print(c)
