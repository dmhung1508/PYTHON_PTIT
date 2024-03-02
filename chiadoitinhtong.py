# import sys
#
# fi = open("a.txt", "r")
# sys.stdin = fi
s = input()
while len(s) > 1:
    x = int(len(s) // 2)  # Sửa thành phép chia nguyên để lấy số nguyên
    a = int(s[x:])
    b = int(s[:x])  # Sửa thành dấu ngoặc vuông [] thay vì dấu ngoặc đơn ()
    s = str(a + b)
    print(s)
