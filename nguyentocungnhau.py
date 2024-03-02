from math import gcd
n,k= map(int,input().split())
l,u = 10**(k-1),10**k
cnt = 0
for i in range(l,u):
    if gcd(i,n) == 1:
        print(i,end=" ")
        cnt += 1
        if cnt %10 == 0:
            print()
      
