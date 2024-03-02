import sys
fi = open("a.txt","r")
sys.stdin = fi
f2 = open("a1.txt","w")
sys.stdout = f2
n,m = map(int,input().split())
list = [int(i) for i in input().split()]
list = sorted(set(list))
n = len(list)
def Try(i,l):
    if len(l)==m:
        print(*l)
    else:
        for j in range(i,n):
            Try(j+1,l+[list[j]])
Try(0,[])