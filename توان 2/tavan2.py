'''
برنامه‌ای بنویسید که عدد nn را از ورودی بخواند و اولین توان عدد دو را که از nn بزرگتر است چاپ کند.
'''

n = int(input())
# n = n+1
for i in range(1,n):
    if (2**i) > n :
        break
print(2**i) 

