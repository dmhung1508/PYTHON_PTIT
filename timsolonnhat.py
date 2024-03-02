n = int(input())
for i in range(n):
    s = input()
    s+= '*'
    ans = -1
    x = 0
    for j in range(len(s)-1):
        if s[j].isdigit():
            x = x * 10 + int(s[j])
            if s[j+1].isalpha():
                ans = max(ans, x)
                x = 0
    ans = max(ans, x)
    print(ans)
