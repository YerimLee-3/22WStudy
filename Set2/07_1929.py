import sys
import math

def isPrime(i):
    if i == 1:
        return False
    elif i == 2:
        return True
    for k in range(2, int(math.sqrt(i))+1):
        if i % k == 0:
            return False
    return True

m, n = map(int, sys.stdin.readline().split())

for k in range(m, n+1):
    if isPrime(k):
        print(k)
