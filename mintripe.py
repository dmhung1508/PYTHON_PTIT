import sys
fi = open("a.txt","r")
sys.stdin = fi
for i in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    print(*a)
    a =list(set(a))
    print(a[0]+a[1]+a[2])