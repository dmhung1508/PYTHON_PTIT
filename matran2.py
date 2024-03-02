# import sys
# fi = open("a.txt","r")
# sys.stdin = fi
t = int(input())
a = [[]]*t
for i in range(t):
    a[i] = [int(i) for i in input().split()]
cnt1,cnt2=0,0
for i in range(t):
    for j in range(t):
        if j > t-i-1:
            cnt1+= a[i][j]
        else:
            if j < t-i-1:
                cnt2+= a[i][j]
k = int(input())
if abs(cnt1-cnt2) <=k:
    print("YES")
else:
    print("NO")
print(abs(cnt1-cnt2))