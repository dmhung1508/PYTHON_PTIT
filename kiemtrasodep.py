t = int(input())
def chckso(m):
    res =""
    for i in m:
        if res.find(i) == -1:
            res += i
            if len(res) == 3:
                return False
    return True
def check(n):
    for i in range(len(n)-2):
        if s[i]!= s[i+2]:
            return False
    return True
        
for i in range(t):
    s = input()
    if chckso(s) and check(s):
        print("YES")
    else:
        print("NO")

    