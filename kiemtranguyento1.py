import sys
fi = open("a.txt","r")
sys.stdin = fi
f2 = open("a1.txt","w")
sys.stdout = f2
from math import *
def ispri(s):
    for i in range(2, int(sqrt(s))+1):
        if s% i == 0:
            return 0
    return 0 if s < 2 else 1
n,m = map(int, input().split())
a = {}
for i in range(n):
    list = [ispri(int(i)) for i in input().split()]
    print(*list)
