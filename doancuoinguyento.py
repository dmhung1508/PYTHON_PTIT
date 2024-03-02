from math import *
def nto(s):
    for i in range(2,int(sqrt(s))+1):
        if s% i == 0:
            return False
    return True if s >1 else False
t = int(input())
for i in range(t):
    s = input()
    s = s[-4:]
    if nto(int(s)):
        print("YES")
    else:
        print("NO")