# import sys
# fi = open("a.txt","r")
# sys.stdin = fi
# t = int(input())
# f2 = open("a1.txt","w")
# sys.stdout = f2
t = int(input())
def check(a,b):
    for i in range(len(a)):
        if a[i] > b[i]:
            return False
    return True
for i in range(t):
    n = int(input())
    a = sorted([int(i) for i in input().split()])
    b = sorted([int(i) for i in input().split()])
    if check(a,b):
        print("YES")
    else:
        print("NO")