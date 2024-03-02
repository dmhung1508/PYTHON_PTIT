# import sys
# fi = open("a.txt","r")
# sys.stdin = fi
# f2 = open("a1.txt","w")
# sys.stdout = f2

t = int(input())

for i in range(t):
    n = int(input())
    list = [int(i) for i in input().split()]
    a = set(list)
    cnt = 0
    for i in a:
        if list.count(i) > n/2:
            print(i)
            cnt = 1
            break
    if cnt ==0:
        print("NO")