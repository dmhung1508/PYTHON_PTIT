t = int(input())
def check(s,a,b,c,n):
    if len(s) == n and a<=b and b <=c and a>0:
        print(s)
        return
    if len(s) > n:
        return
    check(s+'A', a+1,b,c,n)
    check(s+'B',a,b+1,c,n)
    check(s+'C', a,b,c+1,n)
for i in range(3,t+1):
    check('',0,0,0,i)
    