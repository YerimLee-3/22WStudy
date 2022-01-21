import sys

input = sys.stdin.readline

nCount = int(input())
aList = list(map(int, input().split()))

res = min(aList)*max(aList)

print(res)
