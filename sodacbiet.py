import sys

# fi = open("a.txt", "r")
# sys.stdin = fi
t = int(input())
for i in range(t):
    n,m = map(int, input().split())
    k = '{0:b}'.format(m)[::-1]
    pow = 1
    res = 0
    for i in range(len(k)):
        res += pow*int(k[i])
        pow *= n
    print(res%(10**9+7))
