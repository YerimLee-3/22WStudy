import sys

n = int(sys.stdin.readline())
strDict = {}

for i in range(n):
    s = str(sys.stdin.readline().strip())
    strDict[s] = len(s)

strDict2 = dict(sorted(strDict.items()))
strDict3 = sorted(strDict2.items(), key=lambda x:x[1])

for i in strDict3:
    print(i[0])

