
lst = []
n = input()
for i in n :
    lst.append(i)
    
    
for j in lst:
    a = j.center(int(j),j)
    if j == "0" :
        print(f"{int(j)}:")
    else :
        print(f"{int(j)}: {int(a)}")

'''
برنامه‌ای بنويسيد كه یک عدد صحيح را که تعداد ارقامش مشخص نيست از کاربر گرفته و هر رقم را به تعداد آن رقم چاپ کند.

ورودی
در یک خط عدد به شما داده می‌شود. طول عدد از ۱۰۰ کوچکتر است.

خروجی
به ازای هر رقم ابتدا خود آن رقم به همراه ‍: را چاپ کرده سپس به تعداد آن رقم از همان رقم چاپ کنید.

مثال
ورودی نمونه ۱
50943
Copy
خروجی نمونه ۱
5: 55555
0:
9: 999999999
4: 4444
3: 333

'''
