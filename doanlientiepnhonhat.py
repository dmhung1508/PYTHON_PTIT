# import sys
#
# fi = open("a.txt", "r")
# sys.stdin = fi
t = int(input())
for i in range(t):
    n= int(input())
    list = [int(i) for i in input().split()]
    s = []
    for i in range(n):
        while len(s) > 0 and list[i] > list[s[-1]]:
            s.pop()
        if len(s) ==0:
            print(i+1, end=" ")
        else:
            print(i-s[-1], end= " ")
        s.append(i)
    print()