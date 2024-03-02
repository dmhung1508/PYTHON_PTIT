import math
def isPrime(n):
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True
def isEmirp(n):
    if isPrime(n):
        s = str(n)
        for i in s:
            if not isPrime(int(i)):
                return False
        a = sum([int(i) for i in s])
        if not isPrime(a):
            return False
        s = s[::-1]
        if isPrime(int(s)):
            return True
        
    return False
n = int(input())
for i in range(n):
    a = int(input())
    if isEmirp(a):
        print("Yes")
    else:
        print("No")
