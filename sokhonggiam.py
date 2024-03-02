def check(s):
    x = len(s)
    for i in range(x-1):
        if s[i] > s[i+1]:
            return False
    return True
t = int(input())
for i in range(t):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")