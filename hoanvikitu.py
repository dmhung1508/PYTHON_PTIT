import sys
fi = open("a.txt","r")
sys.stdin = fi
f2 = open("a1.txt","w")
sys.stdout = f2
p = input()
n = len(p)
vt = [0]*n
def gen(s):
    if len(s) == n:
        print(s)
    else:
        for i in range(n):
            if vt[i] == 0:
                vt[i] = 1
                gen(s+str(p[i]))
                vt[i] = 0
gen("")