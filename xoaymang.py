n = int(input())
for i in range(n):
    x, y = map(int, input().split())

    list = [int(x) for x in input().split()]
    k = list[y:] + list[:y]
    print(*k)