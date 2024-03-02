import sys

# fi = open("a.txt", "r")
# sys.stdin = fi
t = int(input())
a = []
for i in range(t):
    s =input().split()
    a.append(len(s))
x = []
i = 0
while i < len(a):
    if a[i] == 6:
        x.append(1)
        while  i < len(a) and a[i] != 7:
            i+=1
        continue
    elif a[i] == 7:
        x.append(2)
        i+= 4
        continue
print(len(x))
for i in x:
    print(i)