import sys

fi = open("a.txt", "r")
sys.stdin = fi
s = input()
i = 0
check = 1
while i < len(s):
    if s[i:i+3] == "688":
        i+=3
    else:
        if s[i:i+2] == "68":
            i+=2
        else:
            if s[i] == "6":
                i+=1
            else:
                check = 0
                break
if check == 1 and i == len(s):
    print("YES")
else:
    print("NO")