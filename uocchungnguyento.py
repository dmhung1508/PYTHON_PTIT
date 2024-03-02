from math import *
def isPrime(s):
    if s < 2:
        return False
    for i in range(2,int(sqrt(s)+1)):
        if s % i == 0:
            return False
    return True
def tong(s):
    s= str(s)
    cnt = 0
    for i in s:
        cnt += int(i)
    return isPrime(cnt)
t = int(input())
for i in range(t):
    m,n = map(int,input().split())
    if tong(gcd(m,n)):
        print("YES")
    else:
        print("NO")