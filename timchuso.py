import sys

fi = open("a.txt", "r")
sys.stdin = fi
from decimal import Decimal
from math import *
s = 3 + sqrt(5)
s = float(s)
result = pow(s, 2000000) // (10**9+7)
print(result)

