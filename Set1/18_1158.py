import sys

n, k = map(int, sys.stdin.readline().split())

sit = [i for i in range(1, n+1)]
res = []

flag = 0

for i in range(n):
    flag += k-1
    flag = flag%len(sit)

    res.append(sit.pop(flag))

print("<", end="")
for i in res:
    if i != res[-1]:
        print("%d, " %i, end="")
print("%d>" %res[-1])
