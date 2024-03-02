import sys

fi = open("a.txt", "r")
sys.stdin = fi

f = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    s =""
    while n >0:
        x = n% m
        s = f[x] + s
        n //= m
    print(s)