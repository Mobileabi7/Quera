# اعداد اول

# AF%D8%A7%D9%87-%
# https://b2n.ir/844713

a = int(input())
b = int(input())

for i in range(a, b + 1):
    adad_aval = True
    for x in range(2, i):
        if i % x == 0:
            adad_aval = False
            break
    if adad_aval == True:
        print(i)
