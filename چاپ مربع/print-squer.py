# چاپ مربع
# https://b2n.ir/111929

n = int(input())
between = ("*" + " " * (n - 2) + "*\n") * (n - 2)
print("*" * n, between + "*" * n, sep="\n")