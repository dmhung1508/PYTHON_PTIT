# import sys
# fi = open("a.txt","r")
# sys.stdin = fi
# f2 = open("a1.txt","w")
# sys.stdout = f2
import sys
from math import *
def nto(s):
    for i in range(2,int(sqrt(s))+1):
        if s % 2 == 0:
            return False
    return True
a = [1]*100000
def sang():
    a[1]= a[0]= 0
    for i in range(2,100):
        if (a[i]):
            for j in range(i*i,100000,i):
                a[j] = 0
t = int(sys.stdin.readline())
sang()
for i in range(t):
    s = input()
    m,n = int(s[0:3]),int(s[-3:])

    if a[m] and a[n]:
        print("YES")
    else:
        print("NO")
