X = int(input())
N = int(input())
if N == 0 :
    X = 20
    print(X)
elif N == 7 :
    print(X)
else :
    k = X-N
    if k < 0 :
        X = 0 
        print(X)
    else:
        print(k)


