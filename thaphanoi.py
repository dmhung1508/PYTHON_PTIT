t = int(input())
def thap(n,a,b,c):
    if n == 1:
        print(a+' -> '+c)
        return
    thap(n-1,a,c,b)
    thap(1,a,b,c)
    thap(n-1,b,a,c)
thap(t,'A','B', 'C')