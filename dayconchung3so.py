import math

def solve() :
    n, m, k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    check, i, j, h = 0, 0, 0, 0
    while i < n and j < m and h < k:
        if a[i] == b[j] == c[h] :
            print(a[i], end = " ")
            i, j, h = i + 1, j + 1, h + 1
            check = 1
        elif a[i] < b[j]  : i += 1
        elif b[j] < c[h] : j += 1
        else : h += 1
    if check == 0:
        print("NO", end = "")
    print()

t = 1
t = int(input())
for i in range (t) : solve()
