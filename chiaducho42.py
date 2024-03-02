
cnt = 10
a =[]
while cnt > 0:
    list = [int(i) for i in input().split()]
    cnt -= len(list)
    for i in list:
        a.append(i%42)
print(len(set(a)))