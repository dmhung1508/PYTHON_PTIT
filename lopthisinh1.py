# import sys
#
# fi = open("a.txt", "r")
# sys.stdin = fi

class ts():
    def __init__(self,ten,ns,t,v,a):
        self.ten= ten
        self.ns = ns
        self.t = t
        self.v = v
        self.a = a
    def __str__(self):
        tong = self.t + self.v + self.a
        return (f"{ten} {ns} {tong:.1f}")
if __name__ == "__main__":
    ten = input()
    ns = input()
    t= float(input())
    v = float(input())
    a = float(input())
    rec = ts(ten,ns,t,v,a)
    print(rec)