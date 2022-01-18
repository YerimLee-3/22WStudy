import sys

n = int(sys.stdin.readline())
intSet = set(map(int, sys.stdin.readline().split()))
intList = list(intSet)
intList.sort()

for i in intList:
    print(i, end=" ")