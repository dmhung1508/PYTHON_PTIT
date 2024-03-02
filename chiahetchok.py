a,k,n = map(int,input().split())
x = a //k + 1
cnt = 0
while x*k <=n:
    print(x*k-a,end=' ')
    x+=1
    cnt =1
if cnt == 0:
    print(-1)