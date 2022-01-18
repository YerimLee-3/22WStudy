import sys

n = int(sys.stdin.readline())
nList = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
mList = list(map(int, sys.stdin.readline().split()))

nDict = {}

for i in nList:
    if i in nDict:
        nDict[i] += 1
    else:
        nDict[i] = 1

for k in mList:
    if k in nDict:
        print(nDict.get(k), end=" ")
    else:
        print(0)