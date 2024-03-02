n = int(input())
for i in range(n):
    p1, p2 =input().split()
    a = input().split()
    if len(a) == 1:
        m = a[0]
        n= input()
    else:
        m = a[0]
        n = a[1]
    if p1 > p2:
        p1, p2 = p2, p1
    p = m.replace(p2, p1)
    q = n.replace(p2, p1)
    print(int(p) + int(q), end=' ')
    p = m.replace(p1, p2)
    q = n.replace(p1, p2)
    print(int(p) + int(q))
    