import sys
from math import *
# fi = open("a.txt", "r")
# sys.stdin = fi
def xoay(a,b):
    for i in range(0,len(b)-1):
        c= b[i+1:] + b[0:i+1]
        if c== a:
            return i+1
    return -1
t = int(input())
s = []
for i in range(t):
    s.append(input())
def main():
    ans = 10 ** 9
    for i in s:
        tmp = 0
        for j in s:
            if i != j:
                c = xoay(i,j)
                if c == -1:
                    print(-1)
                    return
                tmp+=c
        ans = min(ans, tmp)
    print(ans)
main()