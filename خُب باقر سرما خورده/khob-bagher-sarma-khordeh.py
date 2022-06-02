
# خُب باقر سرما خورده
# https://b2n.ir/e33907

numbers = []
for i in range(5):
    string = input()
    if "MOLANA" in string or "HAFEZ" in string:
        numbers.append(str(i + 1))
        print(numbers)
print(" ".join(numbers) if len(numbers) else "NOT FOUND!")

# n1 = input()
# n2 = input()
# n3 = input()
# n4 = input()
# n5 = input()
# lst = [n1,n2,n3,n4,n5]
# line_new = []
# for i in lst :
#     if "MOLANA" in i or 'HAFEZ' in i :
#         line_new.append(i)
    
# counter = 0
# for i in line_new :
#     counter += 1

# if counter > 0 :
#     print(counter)
# else :
#     print('NOT FOUND!')
