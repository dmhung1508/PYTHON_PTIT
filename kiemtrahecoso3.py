t = int(input())
def check(s):
    for i in s:
        if i not in {'0','1','2'}:
            return False
    return True
for i in range(t):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")