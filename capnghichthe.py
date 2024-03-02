t = int(input())
a = [int(i) for i in input().split()]
cnt = 0
for i in range(t):
    for j in range(i+1,t):
        if a[i] > a[j]:
            cnt+=1
print(cnt)