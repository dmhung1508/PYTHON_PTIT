# import sys
# fi = open("a.txt","r")
# sys.stdin = fi
# f2 = open("a1.txt","w")
# sys.stdout = f2
t = int(input())
for i in range(t):
    s= input()
    m = input()
    cnt = 0
    start = 0
    while start < len(s):
        start = s.find(m,start)
        if start!=-1:
            cnt+=1
            s = s.replace(m,"",1)
            start+=1
        else:
            break
    print(cnt)
