import sys
fi = open("a.txt","r")
sys.stdin = fi
f2 = open("a1.txt","w")
sys.stdout = f2

from math import *
def nto(s):
    if s <2:
        return False
    for i in range(2,int(sqrt(s))+1):
        if s % 2 == 0:
            return False
    return True
def check(s):
    cnt = 0
    for i in s:
        if(nto(int(i))):
            cnt+=1
    if nto(len(s)) and(cnt >(len(s)-cnt)):
        return True
    else:
        return False
t = int(input())
for i in range(t):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
