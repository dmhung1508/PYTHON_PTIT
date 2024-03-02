# import sys
#
# fi = open("a.txt", "r")
# sys.stdin = fi

from itertools import permutations
t = int(input())
for i in range(t):
    n = int(input())
    arr = [i for i in range(1, n+1, 1)]
    per = permutations(arr,n)
    a = list(per)
    print(len(a))
    a = sorted(a,reverse=True)
    for i in a:
        for j in i:
            print(j,end="")
        print(end = " ")
    print()