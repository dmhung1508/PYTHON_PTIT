import sys

# fi = open("a.txt", "r")
# sys.stdin = fi

from math import *

test=int(input())
c = []
while True:
    try:
        s=input().split()
        for i in s:
            c.append(int(i))
    except EOFError:
        break
j=0
for _ in range(test):

    n, k = c[j], c[j + 1]
    j += 2
    a = []
    # print(n,k)
    for i in range(j, j + n):
        a.append(c[i])
    j = j + n
    ans = 10**9
    for i in range(0, n):
        if a[i] % k == 0:
            for v in range(i, n):

                tmp = gcd(a[i], a[v])
                if tmp == k:
                    ans = min(ans, v - i + 1)
                    break
                elif tmp < k:
                    break
    print(ans if ans != 10 ** 9 else -1)