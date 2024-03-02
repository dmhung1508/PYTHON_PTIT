import sys

is_prime=[1 for _ in range(15001)]

def snt():
    is_prime[0]=is_prime[1]=0
    for i in range(2,15000):
        if is_prime[i]:
            for j in range(i*i,15000,i):
                is_prime[j]=0

a=[]

def main():
    snt()
    for i in range(1,15000-1):
        if is_prime[i]:
            if i**2 < 1e9:
                for j in range(i+1,15000):
                    if is_prime[j]:
                        if i*i*j*j<=1e9:
                            a.append((i**2)*(j**2))
                        else:
                            break
            else:
                break
    for i in range(1,14):
        if is_prime[i]:
            a.append(i**8)
    a.sort()
    n=int(input())
    d=0
    for i in a:
        if i<=n:
            d+=1
        else:
            break
    print(d)



if __name__=='__main__':
    main()