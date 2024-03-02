def solve(n):
    for i in range(1000):
        if n % 7 == 0:
            return n
        rn = int(str(n)[::-1])
        n += rn
    return -1
t = int(input())
for i in range(t):
    s = int(input())
    print(solve(s))
