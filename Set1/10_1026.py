import sys

n = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

res = 0

a.sort()

for i in a:
    res += i*max(b)
    b.remove(max(b))

print(res)

