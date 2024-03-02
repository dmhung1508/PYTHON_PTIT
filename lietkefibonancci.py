a = [1]*100
def fibo():
    a[1]=a[2]=1
    for i in range(3,94):
        a[i]= a[i-1]+ a[i-2]
fibo()
t = int(input())
for i in range(t):
    m,n= map(int,input().split())
    for i in range(m,n+1):
        print(a[i], end=" ")
    print()