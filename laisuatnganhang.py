t =int(input())
for i in range(t):
    n,x,m = map(float,input().split())
    x = x/100
    x = 1+x
    cnt = 0
    while n<m:
        n = n*x
        cnt = cnt +1
    print(cnt)