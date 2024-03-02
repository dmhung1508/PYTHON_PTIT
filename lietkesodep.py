def check(s):
    if len(s) % 2 == 1 or s != s[::-1]:
        return False
    for i in s:
        if i not in '02468':
            return False
    return True
t = int(input())
for i in range(t):
    n = int(input())
    for i in range(22,n,2):
        if check(str(i)):
            print(i, end=' ')
    print("")        
        
