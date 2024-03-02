t = int(input())
from math import *
def isPrime(s):
    for i in range(2,int(sqrt(s))+1):
        if s%i == 0:
            return False
    return True
def check(s):
    cnt = 0
    for i in range(len(s)):
        cnt+= int(s[i])
        if i%2==0:
            if int(s[i])%2 != 0:
                return False
        if i%2==1:
            if int(s[i])%2 != 1:
                return False
    return isPrime(cnt)
for i in range(t):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
