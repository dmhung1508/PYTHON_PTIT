t = int(input())
from math import *
def ngto(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return n>1
for i in range(t):
    s = int(input())
    st = str(s)
    cnt = 0
    for i in st:
        if ngto(int(i)):
            cnt+=1
    if(cnt> len(st)-cnt and ngto(len(st))):
        print("YES")
    else:
        print("NO")