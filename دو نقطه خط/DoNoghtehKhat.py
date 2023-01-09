# دو نقطه خط
# https://b2n.ir/n47769

string = input().split()

if string[0] == string[2]:
    print("Vertical")

elif string[1] == string[3]:
    print("Horizontal")

else:
    print("Try again")