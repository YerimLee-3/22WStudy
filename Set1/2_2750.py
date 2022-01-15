import sys

n = int(sys.stdin.readline())
numSet = set()

for i in range(0,n):
    k = int(sys.stdin.readline())
    numSet.add(k)

for i in sorted(numSet):
    print(i)

