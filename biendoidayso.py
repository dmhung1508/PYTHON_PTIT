# import sys
# fi = open("a.txt","r")
# sys.stdin = fi
# f2 = open("a1.txt","w")
# sys.stdout = f2

while True:
    li = [int(i) for i in input().split()]
    if li.count(0) == 4:
        break
    cnt =0
    while True:
        if li.count(li[0]) == 4:
            print(cnt)
            break
        tmp = li.copy()
        for i in range(4):
            li[i] = abs(tmp[i] - tmp[(i + 1) % 4])
        cnt += 1
