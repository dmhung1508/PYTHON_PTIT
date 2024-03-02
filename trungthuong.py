import sys
fi = open("a.txt","r")
sys.stdin = fi
f2 = open("a1.txt","w")
sys.stdout = f2
t = int(input())
for i in range(t):
    s = {}
    cnt = 0
    n = int(input())
    for i in range(n):
        m = int(input())
        if m in s:
            s[m] +=1
        else:
            s[m] = 1
        cnt = max(cnt,s[m])
    ans = 1001
    for i in s:
        if s[i] == cnt:
            ans = min(ans,i)
    print(ans)

