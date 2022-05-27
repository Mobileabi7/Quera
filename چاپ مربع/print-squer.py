k=int(input('n:'))
def square(n):
    lines = ['*' * (n - i) + " " * i for i in range(n)]
    for l in lines + lines[-2::-1]:
        print(l + l[::-1])
square(k)