t = int(input())
max = 1000000
f = [1]* max
f[0] = f[1] = 0
for i in range(2, max):
    if f[i]:
        for j in range(i*i, max, i):
            f[j] = 0

for i in range(t):
    n = int(input())
    cnt = 0
    for j in range(n-5):
        if (f[j] and f[j+2] and f[j+6]) or (f[j] and f[j+4] and f[j+6]):
            cnt+=1
    print(cnt)