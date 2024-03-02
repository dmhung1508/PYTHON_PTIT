t = int(input())
def tong(s):
    sum = 0
    for i in s:
        sum += int(i)
    return sum
def check(s):
    for i in range(1,len(s)):
        if abs(int(s[i])-int(s[i-1])) != 2:
            return False
    return True
for i in range(t):

    s = input()
    if tong(s)%10 == 0 and check(s):
        print("YES")
    else:
        print("NO")