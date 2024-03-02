import sys

fi = open("a.txt", "r")
sys.stdin = fi
t = input()
t = int(t,2)
ocd = oct(t)
print(ocd[2:])