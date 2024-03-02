nop=int(1e6+1)
nt=[1 for i in range(0, nop)]

def dao(n):
    s=str(n)
    s=s[::-1]
    return int(s)
def sang_nt():
    nt[0]=nt[1]=0
    for i in range(1000):
        if nt[i]:
           for j in range(i*i,nop,i):
               nt[j]=0
def main():
    test=int(input())
    sang_nt()

    for _ in range(test):
        c=0
        n=int(input())
        check=[0]*(n+1)
        for i in range(n):
            if nt[i]:
                j=dao(i)
                if j<=n and i!=j and nt[j] and not check[i] and not check[j]:
                    check[i]=1
                    check[j]=1
                    print(i,j,end=' ')
        print()
if __name__=='__main__':
    main()
