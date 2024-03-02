t = int(input())
def check(s):
    for t in s:
        if t != '4' and t != '7':
            return False
    return True
for i in range(t):
    s = input()
    if check(s):
        print('YES')
    else:
        print('NO')