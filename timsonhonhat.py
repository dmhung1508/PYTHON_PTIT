n = int(input())
for i in range(n):
    s = input()
    ans = float('inf')
    x = 0
    for j in range(len(s)):
        if s[j].isdigit():
            x = x * 10 + int(s[j])
        else:
            if j != 0 and s[j - 1].isdigit():
                ans = min(ans, x)
            x = 0
    print(ans)
