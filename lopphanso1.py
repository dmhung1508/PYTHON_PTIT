# import sys
#
# fi = open("a.txt", "r")
# sys.stdin = fi
from math import *
class ps1():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def rut(self):
        p = gcd(self.x,self.y)
        a = self.x//p
        b = self.y //p
        print(f"{a}/{b}")
if __name__ == "__main__":
    s = input().split()
    x,y = int(s[0]), int(s[1])
    rec = ps1(x,y)
    rec.rut()