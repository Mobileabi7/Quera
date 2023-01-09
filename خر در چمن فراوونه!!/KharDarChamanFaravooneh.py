# خر در چمن فراوونه
# https://b2n.ir/627599

number = (input()).split(" ")

a = int(number[0])
b = int(number[1])
l = int(number[2])

sums = 0

for i in range(1, l + 1):
    if i % 2 != 0:
        sums += a
    else:
        sums += b

print(sums)

###########################################################

number = (input()).split(" ")

a, b, l = int(number[0]), int(number[1]), int(number[2])

sums = 0
count = 1

while count <= l:
    if count % 2 != 0:
        sums += a
    else:
        sums += b
    count += 1

print(sums)