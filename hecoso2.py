# import sys
# fi = open("a.txt","r")
# sys.stdin = fi

t = int(input())
for i in range(t):
    n = int(input())
    s = input()

    de = int(s,2)
    if n == 2:
        print(s)
    if n == 8:
        octal = oct(de)
        print(octal[2:])
    if n == 16:
        hexa = hex(de)
        hexa = hexa.upper()
        print(hexa[2:])
    if n == 4:
        a = ""
        while de >0:
            r = de %n
            a = str(r)+a
            de //= n
        print(a)
