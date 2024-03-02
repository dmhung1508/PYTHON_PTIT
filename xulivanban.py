import sys
fi = open("a.txt","r")
sys.stdin = fi
import re
text = ""
while True:
    try:
        s = input().lower()
        text += s+ " "
    except:
        break
line = re.split("[.!?]\s*",text)
line.remove("")
for i in line:
    i = (i[0].upper()+ i[1:]).split()
    i = " ".join(i)
    print(i)