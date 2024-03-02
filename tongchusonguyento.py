t = int(input())
from math import *
def isPrime(s):
    for i in range(2,int(sqrt(s))+1):
        if s%i==0:
            return False
    return True
def check(s):
    cnt = 0
    for i in s:
        cnt+= int(i)
    return isPrime(cnt)
for i in range(t):
    s = input()
    if (check(s)):
        print("YES")
    else:
        print("NO")