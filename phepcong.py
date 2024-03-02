s = input()
a = s.split(" ")
m,n,p = int(a[0]),int(a[2]),int(a[4])
if m+n == p:
    print("YES")
else:
    print("NO")