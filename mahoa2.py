p = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'




while True:
    s = input()
    if s == "0":
        break
    s,x = s.split()
    s = int(s)
    res = ''

    for i in x:
        j = p.find(i)
        res += p[(j+s)%28]

    print(res[::-1])
