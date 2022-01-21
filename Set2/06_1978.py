import math
import sys

def isPrime(num):
    if i == 1:
        return False
    elif i == 2:
        return True
    for k in range(2, int(math.sqrt(i))+1):
        if i % k == 0:
            return False
    return True

input = sys.stdin.readline

n = int(input())
nList = list(map(int, input().split()))

cnt = 0
flag = True

for i in nList:
    if isPrime(i):
        cnt += 1
    


print(cnt)
