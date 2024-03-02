# import sys
#
# fi = open("a.txt", "r")
# sys.stdin = fi
class Rectangle():
    def __init__(self,d,r,m):
        self.d = d
        self.r = r
        self.m = m
    def area(self):
        return self.d*self.r
    def perimeter(self):
        return (self.d+self.r)*2
    def color(self):
        return self.m[0].upper() + self.m[1:].lower()


arr = input().split()
if int(arr[0]) > 0 and int(arr[1]) > 0:
    r = Rectangle(int(arr[0]), int(arr[1]), str(arr[2]))
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
else:
    print('INVALID')