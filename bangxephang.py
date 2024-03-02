# import sys
# fi = open("a.txt","r")
# sys.stdin = fi
t = int(input())
a = []
for i in range(t):
    list = []
    list.append((input()))
    c,t = map(int, input().split())
    list.append(c)
    list.append(t)
    a.append(list)
a = sorted(sorted(sorted(a,key = lambda x: x[0]), key = lambda x: x[2]),key = lambda x:x[1], reverse= True)
for i in a:
    print(*i)