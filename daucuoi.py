t = int(input())
for i in range(t):
    s = input()
    a = s[-2:]
    b = s[:2]

    
    if a == b:
        print('YES')
    else:
        print('NO')