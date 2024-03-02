from math import *
t = int(input())
for i in range(t):
    a = input()
    b = a[::-1]
    a = int(a)
    b = int(b)
    if gcd(a,b) == 1:
        print("YES")
    else:
        print("NO")