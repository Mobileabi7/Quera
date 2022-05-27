r = input()
u = 0
for i in r :
    if i == 'R' :
        u += 1
    elif i == 'Y' :
        u += 0.75

if u >= 3 :
    print('nakhor lite')
elif r =='RRRRR' or r == 'YYYYY' :
    print('nakhor lite')
else :
    print('rahat baash')



