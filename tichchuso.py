t = int(input())
def check(s):
    cnt = 1
    for i in s:
        if i != '0':
            cnt *= int(i)
    return cnt
for i in range(t):
    s = input()
    print(check(s))