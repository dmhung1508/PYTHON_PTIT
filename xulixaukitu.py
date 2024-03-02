

m = input().lower().split()
n = input().lower().split()
p = sorted(set(list(m+n)))
print(*p)
p = []
for i in m:
    if  i  in n:
        p.append(i)
print(*sorted(set(p)))


