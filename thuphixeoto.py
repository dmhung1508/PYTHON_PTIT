# import sys
#
# fi = open("a.txt", "r")
# sys.stdin = fi

fee = {
    "Xe_con5": 10000,
    "Xe_con7": 15000,
    "Xe_tai2": 20000,
    "Xe_khach29": 50000,
    "Xe_khach45": 70000,
}
t = int(input())
na = {}
for i in range(t):
    s = input().split()
    name = s[1] + s[2]
    if s[3] == "IN":
        if str(s[4]) not in na:
            na[str(s[4])] = 0
        na[str(s[4])] += fee[name]

for i in na:
    print(f"{i}: {na[i]}")