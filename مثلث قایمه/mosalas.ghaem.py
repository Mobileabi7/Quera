#برنامه‌ای بنویسید که سه عدد صحیح مثبت را به عنوان ورودی از کاربر دریافت کند و در صورتی که امکان ساخت مثلث قائم الزاویه با طول اضلاع داده شده وجود داشته باشد YES و در غیر این صورت NO چاپ کند
#a**2+b**2 = c**2
a = int(input())
b = int(input())
c = int(input())

if ((a**2+b**2) == c**2) or ((a**2+c**2) == b**2) or ((c**2+b**2) == a**2) :
    print("YES")
else :
    print("NO")