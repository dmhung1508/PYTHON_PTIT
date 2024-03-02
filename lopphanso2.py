# import sys
#
# fi = open("a.txt", "r")
# sys.stdin = fi
from math import *
class ps1():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def cong(self,ot):
        tu = (self.x*ot.y) + (self.y*ot.x)
        mau= self.y * ot.y
        p = gcd(tu,mau)
        print(f"{tu//p}/{mau//p}")
    def rut(self):
        p = gcd(self.x,self.y)
        a = self.x//p
        b = self.y //p
        print(f"{a}/{b}")
if __name__ == "__main__":
    s = input().split()
    x,y = int(s[0]), int(s[1])
    z,t = int(s[2]), int(s[3])
    rec = ps1(x,y)
    bec = ps1(z,t)
    rec.cong(bec)