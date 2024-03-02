def mul(s):
    x = 1
    for i in s:
        x *= int(i)
    return x
t = int(input())
for i in range(t):
    n = int(input())
    a = [str(i) for i in input().split()]
    a.sort(key= lambda s: (mul(s), int(s)))
    print(*a)