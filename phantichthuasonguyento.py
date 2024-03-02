t = int(input())
def check(x):
    j= 2
    while x>1:
        cnt = 0
        while x % j == 0:
            cnt += 1
            x //= j
        if cnt:
            print("* "+str(j) +"^" +str(cnt), end=" ")
        j += 1
for i in range(t):
    a = int(input())
    print("1 ", end="")
    check(a)
    print()

    