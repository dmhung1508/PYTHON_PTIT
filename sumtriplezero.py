n = int(input())
for l in range(n):
    m = int(input())
    list = [int(x) for x in input().split()]
    list.sort()
    o = len(list)
    cnt = 0
    for i in range(o):
        j = i + 1
        k = o - 1
        while j < k:
            if list[i] + list[j] + list[k] == 0:
                cnt += 1
                j += 1
            elif list[i] + list[j] + list[k] < 0:
                j += 1
            else:
                k -= 1
    print(cnt)