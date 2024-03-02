t = int(input())
def check(s):
    cnt = 0
    for i in s:
        cnt+= int(i)
    s = str(cnt)
    if len(s) == 1:
        return False
    return s== s[::-1]
for i in range(t):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")