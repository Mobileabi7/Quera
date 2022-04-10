n = int(input())
accumulator = 0
for i in range(1, n+1):
    if n%i == 0 and n%2 != 0:
        accumulator+=1
if accumulator==2:
    print('zoj') #barax
else:
    print('fard') #barax