import sys

fi = open("CONTACT.in", "r")
sys.stdin = fi

a = set()
while True:
    try:
        s = input().lower()
        a.add(s)
    except:
        break
a = sorted(a)
for i in a:
    print(i)
