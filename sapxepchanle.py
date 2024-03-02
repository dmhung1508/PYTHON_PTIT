import sys
fi = open("a.txt","r")
sys.stdin = fi
t = int(input())
a= []
while True:
    try:
        list = [int(i) for i in input().split()]
        a +=list
    except:
        break

le = [x for x in a if x%2==1]
chan = [x for x in a if x%2==0]
le.sort()
chan.sort(reverse = True)
for i in a:
    if i%2 == 0:
        print(chan[-1],end = " ")
        chan.pop()
    else:
        print(le[-1], end= " ")
        le.pop()