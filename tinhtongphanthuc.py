t = int(input())
for i in range(t):
    n = int(input())
    if (n%2 == 0):
        s= 0
        for j in range(2,n+1,2):
            s += 1/j
        print("{:.6f}".format(s))
    else:
        s= 0
        for j in range(1,n+1,2):
            s += 1/j
        print("{:.6f}".format(s))