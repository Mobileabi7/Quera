# آخ جون طرف نیست!
# https://b2n.ir/s82371

n1 = input()
string1 = input().split()
n2 = input()
string2 = input().split()
n3 = input()
string3 = input().split()

days = ["shanbe", "1shanbe", "2shanbe", "3shanbe", "4shanbe", "5shanbe", "jome"]
for string in [string1, string2, string3]:
    for i in string:
        if i in days:
            days.remove(i)
print(len(days))