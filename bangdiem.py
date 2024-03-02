# import sys
#
# fi = open("a.txt", "r")
# sys.stdin = fi
id = 1
class bang():
    def __init__(self,ten,diem):
        global id
        self.mahs = 'HS{:02d}'.format(id)
        id+=1
        self.ten = ten
        x = (diem[0] + diem[1]) *2
        for i in range(2, 10):
            x += diem[i]
        self.diemtrungbinh = round(x / 12 + 0.01, 1)
        x /= 12
        if x < 5:
            self.xepLoai = 'YEU'
        elif x < 7:
            self.xepLoai = 'TB'
        elif x < 8:
            self.xepLoai = 'KHA'
        elif x < 9:
            self.xepLoai = 'GIOI'
        else:
            self.xepLoai = 'XUAT SAC'


    def output(self):
        print(self.mahs,self.ten,self.diemtrungbinh, self.xepLoai)
t = int(input())
a = []
for i in range(t):
    ten = input()
    dem = [float(i) for i in input().split()]
    a.append(bang(ten,dem))
a = sorted(a, key= lambda x : (- x.diemtrungbinh, x.mahs))

for i in a:
    i.output()

