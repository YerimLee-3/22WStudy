# 22WStudy
# 1920

import sys

def findX(num, numSet):
    if num in numSet:
        return 1
    return 0

n = int(sys.stdin.readline())
nList = set(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
mList = list(map(int, sys.stdin.readline().split()))

for i in mList:
    res = findX(i, nList)
    print(res)



