t = int(input())
def check(s):
    if s[0] == s[1] or len(s) % 2 == 0:
        return False
    c = s[0]
    for i in range(2,len(s),2):
        if s[i] != s[0]:
            return False
    return True
for i in range(t):
    if check(input()):
        print("YES")
    else:
        print("NO")

