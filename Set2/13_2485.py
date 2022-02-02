from math import gcd
import sys

def findMin(nPos, nSpace):

    m = gcd(nSpace[0], nSpace[1])
    
    for i in range(2, len(nSpace)):
        m = gcd(m, nSpace[i])

    num = 0

    for i in nSpace:
        num += i/m -1
    return num

input = sys.stdin.readline

n = int(input())
nPos = []
nSpace = []

for _ in range(n):
    nPos.append(int(input()))
    if len(nPos) > 1:
        nSpace.append(nPos[-1] - nPos[-2])

res = int(findMin(nPos, nSpace))

print(res)
