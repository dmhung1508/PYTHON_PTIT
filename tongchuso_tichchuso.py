# import sys
# fi = open("a.txt","r")
# sys.stdin = fi
def tong(s):
    to ,tich=0,1
    cnt = 0
    for i in range(len(s)):
        if i%2 ==0:
            to+= int(s[i])
        else:
            if(int(s[i])!= 0):
                cnt+=1
                tich *= int(s[i])
    if cnt == 0:
        tich=0
    return to,tich

t = int(input())
for i in range(t):
    s = input()
    a,b= tong(s)
    print(a,b)
