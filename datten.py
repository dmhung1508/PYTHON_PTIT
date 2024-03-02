
from itertools import *
n,m = map(int,input().split())
d = sorted(set(str(i) for i in input().split()))
k = combinations(d,m)
for i in k:
    print(*i)