t = int(input())
a = [1]*10
a[1] = 1
a[0]= 1
for i in range(2,10):
    a[i] = a[i-1]*i
for i in range(t):
    s = input()
    ans = 0
    for j in s:
        ans+=a[int(j)]
    if ans == int(s):
        print("Yes")
    else:
        print("No")
