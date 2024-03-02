import sys
fi = open("a.txt","r")
sys.stdin = fi
f2 = open("a1.txt","w")
sys.stdout = f2
t = int(input())
def tong(s):
    s = str(s)
    cnt = 0
    for i in s:
        cnt+= int(i)
    return cnt
for i in range(t):
    n = int(input())
    to = []
    list = [str(i) for i in input().split()]
    list.sort(key = lambda s: (sum(int(i) for i in s), int(s)))
    print(*list)

